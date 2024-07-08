import pandas as pd

def check_columns_presence(train_file, test_file):
    # Columns to check
    numerical_columns = ['last_fico_range_high', 'last_fico_range_low', 'collection_recovery_fee',
                         'total_pymnt_inv', 'int_rate', 'fico_range_high']
    categorical_columns = ['debt_settlement_flag', 'sub_grade', 'grade', 'term']
    target_col_name = 'loan_condition_num'

    # Read CSV files
    train_df = pd.read_csv(train_file)
    test_df = pd.read_csv(test_file)

    print(f"Checking columns in {train_file}:")
    check_columns(train_df, numerical_columns, categorical_columns, target_col_name)

    print(f"\nChecking columns in {test_file}:")
    check_columns(test_df, numerical_columns, categorical_columns, target_col_name)

def check_columns(df, numerical_columns, categorical_columns, target_col_name):
    missing_columns = []

    # Check numerical columns
    for col in numerical_columns:
        if col not in df.columns:
            missing_columns.append(col)

    # Check categorical columns
    for col in categorical_columns:
        if col not in df.columns:
            missing_columns.append(col)

    # Check target column
    if target_col_name not in df.columns:
        missing_columns.append(target_col_name)

    # Print results
    if len(missing_columns) == 0:
        print("All required columns are present.")
    else:
        print("Missing columns:")
        for col in missing_columns:
            print(f"- {col}")

if __name__ == "__main__":
    train_file = r'F:\netsol_project\task_1\credit_decisioning_risk_assesment\artifacts\train.csv'
    test_file = r'F:\netsol_project\task_1\credit_decisioning_risk_assesment\artifacts\test.csv'
    check_columns_presence(train_file, test_file)
