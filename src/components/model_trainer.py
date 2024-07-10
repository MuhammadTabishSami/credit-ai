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
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, X_train, X_test, y_train, y_test, preprocessor_path):
        try:
            logging.info('Starting model training...')

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

            for model_name, model in models.items():
                try:
                    model.fit(X_train, y_train)
                    logging.info(f'Model {model_name} training has been completed.')
                except Exception as e:
                    logging.error(f'Error training model {model_name}: {e}')
                    raise CustomException(e, sys)

            model_report = evaluate_model(X_train=X_train, y_train=y_train,
                                          X_test=X_test, y_test=y_test, models=models)

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            logging.info(f'Best model found: {best_model_name} with score {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            accuracy = accuracy_score(y_test, predicted)
            logging.info(f'Accuracy: {accuracy}')

            cm = confusion_matrix(y_test, predicted)
            logging.info(f'Confusion Matrix:\n{cm}')

            clf_report = classification_report(y_test, predicted)
            logging.info(f'Classification Report:\n{clf_report}')

            return accuracy, cm, clf_report

        except Exception as e:
            logging.error(f'Error in initiate_model_trainer: {e}')
            raise CustomException(e, sys)
