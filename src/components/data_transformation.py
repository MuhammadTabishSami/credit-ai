import os
import sys
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocess.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self, numerical_columns, categorical_columns):
        try:
            # Numerical Columns Transformer Pipeline
            numerical_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            # Categorical Columns Transformer Pipeline
            categorical_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))  # Removed sparse argument
            ])

            # Combining both transformers into one
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numerical_pipeline, numerical_columns),
                    ('cat', categorical_pipeline, categorical_columns)
                ],
                sparse_threshold=0
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_data_path, test_data_path, target_col_name):
        try:
            # Reading train and test data
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info('Read train and test data completed')

            # Select numerical and categorical columns, excluding the target column
            numerical_columns = train_df.select_dtypes(include=['number']).columns.tolist()
            numerical_columns = [col for col in numerical_columns if col != target_col_name]
            categorical_columns = train_df.select_dtypes(include=['object', 'category']).columns.tolist()
            categorical_columns = [col for col in categorical_columns if col != target_col_name]

            preprocessor = self.get_data_transformer_object(numerical_columns, categorical_columns)
            logging.info(f'Obtained preprocessor object of type: {type(preprocessor)}')

            # Preprocess features
            X_train = preprocessor.fit_transform(train_df[numerical_columns + categorical_columns])
            X_test = preprocessor.transform(test_df[numerical_columns + categorical_columns])

            logging.info('Preprocessing features completed.')

            # Transforming target variable into numerical values
            train_df['loan_condition_encoded'] = train_df[target_col_name].apply(lambda x: 1 if x == 'Good Loan' else 0)
            test_df['loan_condition_encoded'] = test_df[target_col_name].apply(lambda x: 1 if x == 'Good Loan' else 0)

            # Ensure y_train and y_test are numpy arrays of integers
            y_train = train_df['loan_condition_encoded'].values
            y_test = test_df['loan_condition_encoded'].values

            logging.info('Transforming target variable completed.')

            # Save the updated train and test dataframes
            train_df.to_csv(train_data_path, index=False)
            test_df.to_csv(test_data_path, index=False)

            # Saving the preprocessor object
            os.makedirs(os.path.dirname(self.data_transformation_config.preprocessor_obj_file_path), exist_ok=True)
            joblib.dump(preprocessor, self.data_transformation_config.preprocessor_obj_file_path)

            logging.info('Preprocessor pickle file saved.')

            return (
                X_train,
                X_test,
                y_train,
                y_test,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)
