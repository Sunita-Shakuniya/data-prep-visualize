import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from DataCleaning.forms import UploadFileForm, OperationForm
from .utils import perform_data_operations

def index(request):
    return render(request, 'DataCleaning/index.html')
'''
# perfoming operation
def perform_data_operations(file_path, selected_operation, selected_columns=None):
    print(f"Performing operation: {selected_operation} on columns: {selected_columns}")

    # Load the data from the file
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        return None  # Handle unsupported file formats as needed

    # Print column names before deletion
    print("Columns before deletion:", data.columns)

    # Perform data operations based on the selected operation
    if selected_operation == 'delete_column' and selected_columns:
        # Example: Delete selected columns
        data = data.drop(columns=selected_columns, errors='ignore')

    # Print column names after deletion
    print("Columns after deletion:", data.columns)

    # Save the updated data back to the file
    data.to_csv(file_path, index=False)  # You can adjust this based on your needs
'''


# Hnadling the uploaded file path
def handle_uploaded_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES['file']
            
            file_path = default_storage.save('' + uploaded_file.name, ContentFile(uploaded_file.read()))

            # Store the file path in the session to pass it to the data_cleaning view
            request.session['file_path'] = "media/"+file_path

            # Redirect to the data_cleaning view
            return redirect('data_cleaning')

    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form})


# Data cleanin function
def data_cleaning(request):
    file_path = request.session.get('file_path', None)

    if file_path:
        # Print some debugging information
        print(f"File Path in data_cleaning: {file_path}")

        # Read file into a pandas DataFrame
        if file_path.endswith('.csv'):
            data= pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            data =  pd.read_excel(file_path)
        else:
            pass 

        # Set a limit for the number of rows to display and edit
        row_limit = request.session.get('row_limit', 100)
        data = data.head(row_limit)

        # Convert the DataFrame to a list of dictionaries
        data_list = data.to_dict(orient='records')

        return render(request, 'DataCleaning/data_cleaning.html', {'data_list': data_list, 'file_path': file_path})
    else:
        return render(request, 'DataCleaning/data_cleaning.html', {'error_message': 'Invalid file path'})


# Reload function to load more data
def reload_data(request):
    # Get the current row limit from the session
    row_limit = request.session.get('row_limit', 100)

    # Increment the row limit by 100 for the next reload
    row_limit += 100

    # Save the updated row limit back to the session
    request.session['row_limit'] = row_limit

    # Redirect back to the original page for rendering
    return HttpResponse(status=204) 

# Define the get_available_columns function
def get_available_columns(file_path):
    # Implement logic to dynamically get available columns from the file
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        return []
    
    # Dynamically get available columns
    available_columns = list(data.columns)
    print(f"Available Columns: {available_columns}")
    return available_columns

# Getting the request
def perform_operation(request):
    file_path = request.session.get('file_path', None)    

    # Dynamically get available columns
    available_columns = get_available_columns(file_path)

    if request.method == 'POST':
        # Pass available columns to the form when initializing it
        operation_form = OperationForm(request.POST, available_columns=available_columns)
        if operation_form.is_valid():
            selected_operation = operation_form.cleaned_data['operation']
            selected_columns = operation_form.cleaned_data.get('column_name', [])

            # Print debug information
            print(f"Performing operation: {selected_operation} on columns: {selected_columns}")

            # Perform data operations using the new function
            perform_data_operations(file_path, selected_operation, selected_columns)

    # Redirect back to the data cleaning page after performing the operation
    return redirect('data_cleaning')

# Visualization part
def data_visualization(request):
    # Add your logic for the data visualization page
    return render(request, 'DataCleaning/data_visualization.html')    





