import sys
import os
from dataclasses import dataclass
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()  # ModelTrainerConfig initialization

    def initiate_model_trainer(self, train_array, test_array, preprocessor_path):
        try:
            logging.info('Split Training and Test Input Data')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            # Convert sparse matrix to dense array if needed
            if hasattr(X_train, 'toarray'):
                X_train = X_train.toarray()
            if hasattr(X_test, 'toarray'):
                X_test = X_test.toarray()

            # Convert y_train and y_test to dense arrays if needed
            if hasattr(y_train, 'toarray'):
                y_train = y_train.toarray().ravel()
            if hasattr(y_test, 'toarray'):
                y_test = y_test.toarray().ravel()

            # Ensure y_train and y_test are numpy arrays of integers
            y_train = y_train.astype(int)
            y_test = y_test.astype(int)

            models = {
                'Logistic Regression': LogisticRegression(),
                'Decision Tree Classifier': DecisionTreeClassifier(),
                'Random Forest Classifier': RandomForestClassifier(),
                'Support Vector Machine': SVC(),
                'K-Nearest Neighbor': KNeighborsClassifier(),
                'Gaussian Naive Bayes': GaussianNB(),
                'XGB': XGBClassifier()
            }

            # Parameters for Hyperparameter tuning
            # param_grid = {
            #     'Decision Tree Classifier': {
            #         'criterion': ['gini', 'entropy'],
            #         'max_depth': [None, 10, 20, 30, 40, 50],
            #         'min_samples_split': [2, 5, 10],
            #         'min_samples_leaf': [1, 2, 4]
            #     },
            #     'Random Forest Classifier': {
            #         'n_estimators': [100, 200, 300, 400, 500],
            #         'max_features': ['auto', 'sqrt', 'log2'],
            #         'max_depth': [None, 10, 20, 30, 40, 50],
            #         'min_samples_split': [2, 5, 10],
            #         'min_samples_leaf': [1, 2, 4]
            #     },
            #     'XGB': {
            #         'learning_rate': [0.01, 0.05, 0.1, 0.15, 0.2],
            #         'max_depth': [3, 5, 7, 9, 11],
            #         'min_child_weight': [1, 3, 5, 7],
            #         'gamma': [0, 0.1, 0.2, 0.3, 0.4],
            #         'subsample': [0.6, 0.7, 0.8, 0.9, 1.0],
            #         'colsample_bytree': [0.5],
            #         'reg_alpha': [1e-5, 1e-2, 0.1, 1, 100]
            #     },
            #     'Support Vector Machine': {
            #         'C': [0.1, 1, 10, 100],
            #         'gamma': [0.001, 0.01, 0.1, 1],
            #         'kernel': ['linear', 'poly', 'rbf', 'sigmoid']
            #     },
            #     'K-Nearest Neighbor': {
            #         'n_neighbors': [3, 5, 7, 9, 11],
            #         'weights': ['uniform', 'distance'],
            #         'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
            #     },
            #     'Gaussian Naive Bayes': {
            #         'var_smoothing': [1e-9, 1e-8, 1e-7, 1e-6, 1e-5]
            #     },
            #     'Logistic Regression': {
            #         'C': [0.001, 0.01, 0.1, 1, 10, 100],
            #         'solver': ['liblinear', 'lbfgs', 'saga'],  # Changed solver options
            #         'max_iter': [100, 200, 300, 400, 500]
            #     }
            # }

            # # Perform GridSearchCV for each model
            # grid_searches = {}
            # for model_name, model in models.items():
            #     if model_name in param_grid:
            #         grid_search = GridSearchCV(estimator=model,
            #                                    param_grid=param_grid[model_name],
            #                                    scoring='accuracy',
            #                                    cv=5,
            #                                    verbose=1,
            #                                    n_jobs=-1)
            #         grid_search.fit(X_train, y_train)
            #         grid_searches[model_name] = grid_search

            # # Evaluate and select best model
            # best_model_name = None
            # best_accuracy = -1
            # for model_name, grid_search in grid_searches.items():
            #     if grid_search.best_score_ > best_accuracy:
            #         best_accuracy = grid_search.best_score_
            #         best_model_name = model_name

            # best_model = grid_searches[best_model_name].best_estimator_
            # logging.info(f'Best model found: {best_model_name}')

            # Fit each model to the training data
            for model_name, model in models.items():
                try:
                    model.fit(X_train, y_train)
                    
                except TypeError as te:
                    if 'Sparse data was passed' in str(te):
                        raise TypeError("Ensure y_train and y_test are dense numpy arrays of integers.")

            model_report = evaluate_model(X_train=X_train, y_train=y_train,
                                          X_test=X_test, y_test=y_test, models=models)

            # Get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            # Get best model name from dictionary
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            logging.info(f'Best found model on training and testing dataset: {best_model_name}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            # Predict on test set
            predicted = best_model.predict(X_test)

            accuracy = accuracy_score(y_test, predicted)
            logging.info(f'Accuracy: {accuracy}')

            # Print confusion matrix
            cm = confusion_matrix(y_test, predicted)
            logging.info(f'Confusion Matrix:\n{cm}')

            # Print classification report
            clf_report = classification_report(y_test, predicted)
            logging.info(f'Classification Report:\n{clf_report}')

            return accuracy, cm, clf_report

        except Exception as e:
            raise CustomException(e, sys)
