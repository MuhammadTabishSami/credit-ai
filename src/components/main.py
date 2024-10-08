# main.py

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

target_col_name = 'loan_condition'

if __name__ == '__main__':
    # Step 1: Data Ingestion
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

    # Step 2: Data Transformation
    data_transformation = DataTransformation()
    X_train, X_test, y_train, y_test, preprocessor_path = data_transformation.initiate_data_transformation(train_data_path, test_data_path,target_col_name)

    # Step 3: Model Training
    model_trainer = ModelTrainer()
    accuracy,cm,clf_report=model_trainer.initiate_model_trainer(X_train, X_test, y_train, y_test, preprocessor_path)
    
    # Print accuracy score
    print(f'Accuracy: {accuracy}')

     # Print accuracy score
    print(f'Confusion Matrix:\n{cm}')

     # Print accuracy score
    print(f'Classification Report:\n{clf_report}')

