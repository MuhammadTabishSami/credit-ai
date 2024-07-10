import pandas as pd
from data_transformation import DataTransformation

# Sample data to test the transformation

data = {
    'last_fico_range_high':[700,750,800],
    'last_fico_range_low':[650,680,720],
    'collection_recovery_fee':[0.0,12.5,0.0],
    'total_pymnt_inv':[5000,3000,4000],
    'int_rate':[0.15,0.12,0.10],
    'fico_range_high':[700,750,800],
    'debt_settlement_flag':['N','Y','N'],
    'grade':['B','C','A'],
    'sub_grade':['B5','C2','C5'],
    'term':['36 months','60 months','36 months']
    }

df = pd.DataFrame(data)

numerical_columns = ['last_fico_range_high', 'last_fico_range_low', 'collection_recovery_fee', 'total_pymnt_inv', 'int_rate', 'fico_range_high']
categorical_columns = ['debt_settlement_flag', 'sub_grade', 'grade', 'term']

# Initialize the DataTransformation class
data_transformation = DataTransformation()

# Get the preprocessor object
preprocessor = data_transformation.get_data_transformer_object(numerical_columns,categorical_columns)


# Fit and transform the data
transformed_data = preprocessor.fit_transform(df)

#printing the transformed data
print(transformed_data)

#printing the type of transformed data:
print(type(transformed_data))


# Print the preprocessor object to inspect its structure
print(preprocessor)

# Inspect individual components of the preprocessor
print(preprocessor.transformers_)
print(preprocessor.transformers_[0][1])  # Inspect the numerical pipeline
print(preprocessor.transformers_[1][1])  # Inspect the categorical pipelin

