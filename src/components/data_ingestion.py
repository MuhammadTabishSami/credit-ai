# Importing Libraries:
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered the Data Ingestion Component')
        try:
            df = pd.read_csv(r'F:\netsol_project\task_1\raw\preprocessed\processed_file.csv')
            logging.info('Read the Dataset from Source as Dataframe')

            # Selecting columns of interest
            columns_of_interest = ['last_fico_range_high', 'last_fico_range_low', 'collection_recovery_fee',
                                   'total_pymnt_inv', 'int_rate', 'fico_range_high','debt_settlement_flag', 
                                   'sub_grade', 'grade', 'term','loan_condition']

            df = df[columns_of_interest]

            logging.info('Selected columns of interest')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Splitting into train and test sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=56)

            # Saving train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Train and Test sets saved.')

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
