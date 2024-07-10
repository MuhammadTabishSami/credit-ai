import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging
import joblib

class PredictPipeline:
    def __init__(self):
        self.model = self.load_model('artifacts/model.pkl')
        self.preprocessor = self.load_preprocessor('artifacts/preprocess.pkl')

    def load_model(self, file_path):
        try:
            model = joblib.load(file_path)
            logging.info(f'Loaded object of type: {type(model)} from {file_path}')
            return model
        except Exception as e:
            raise CustomException(f'Error loading model from {file_path}', e)

    def load_preprocessor(self, file_path):
        try:
            preprocessor = joblib.load(file_path)
            logging.info(f'Loaded object of type: {type(preprocessor)} from {file_path}')
            return preprocessor
        except Exception as e:
            raise CustomException(f'Error loading preprocessor from {file_path}', e)

    def predict(self, X):
        try:
            if not hasattr(self.preprocessor, 'transform'):
                raise CustomException('Loaded preprocessor is not a transformer')
            X_preprocessed = self.preprocessor.transform(X)
            predictions = self.model.predict(X_preprocessed)
            return predictions
        except Exception as e:
            raise CustomException(e, sys)


# class PredictPipeline:
#     def __init__(self):
#         pass

#     # work as predict.py for incoming inputs from HTML
#     def predict(self,features):
#         try:
#             model_path = r'artifacts\model.pkl'
#             preprocessor_path = r'artifacts\preprocess.pkl'
#             model = load_object(file_path=model_path)
#             preprocessor = load_object(file_path=preprocessor_path)
#             logging.info(f'Loaded preprocessor object of type: {type(preprocessor)}')

#             # Checking if preprocessor is a transformer
#             if not hasattr(preprocessor,'transform'):
#                 raise CustomException('Loaded preprocessor is not a transformer',e)

#             data_scaled=preprocessor.transform(features)
#             preds = model.predict(data_scaled)
#             return preds
#         except Exception as e:
#             raise CustomException(e,e)

# CustomData will be responsible for mapping the input from html to backend.
class CustomData:
    def __init__(self,
        last_fico_range_high: float,
        last_fico_range_low: float,
        collection_recovery_fee: float,
        total_pymnt_inv: float,
        int_rate: float,
        fico_range_high: float,
        debt_settlement_flag: str,
        sub_grade: str,
        grade: str,
        term: str):
        
        """
        Initialize CustomData with specified attributes.
        """
        self.last_fico_range_high = last_fico_range_high
        self.last_fico_range_low = last_fico_range_low
        self.collection_recovery_fee = collection_recovery_fee
        self.total_pymnt_inv = total_pymnt_inv
        self.int_rate = int_rate
        self.fico_range_high = fico_range_high
        self.debt_settlement_flag = debt_settlement_flag
        self.sub_grade = sub_grade
        self.grade = grade
        self.term = term

# This function will return all the input in the form of dataframe
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict ={
            'last_fico_range_high': [self.last_fico_range_high],
            'last_fico_range_low': [self.last_fico_range_low],
            'collection_recovery_fee': [self.collection_recovery_fee],
            'total_pymnt_inv': [self.total_pymnt_inv],
            'int_rate': [self.int_rate],
            'fico_range_high': [self.fico_range_high],
            'debt_settlement_flag': [self.debt_settlement_flag,],
            'sub_grade': [self.sub_grade],
            'grade': [self.grade],
            'term': [self.term] 
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e,sys.exc_info())
    

