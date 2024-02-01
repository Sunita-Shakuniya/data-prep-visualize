# DataScience/utils.py

import pandas as pd
import string
def perform_data_operations(file_path, selected_operation, selected_columns=None):
    print(f"Performing operation: {selected_operation} on columns: {selected_columns}")

    # Load the data from the file
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        return None  # Handle unsupported file formats as needed

    # Perform data operations based on the selected operation
    if selected_operation == 'delete_column' and selected_columns:
        # Example: Delete selected columns
        data = data.drop(columns=selected_columns, errors='ignore')
    elif selected_operation == 'punctuation':
        # Example: Remove punctuation from selected columns
        if selected_columns:
            for col in selected_columns:
                data[col] = data[col].apply(lambda x: ''.join(char for char in str(x) if char not in string.punctuation))

    # Save the updated data back to the file
    data.to_csv(file_path, index=False)  # You can adjust this based on your needs
