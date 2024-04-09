import pandas as pd
import plotly.express as px
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from DataCleaning.forms import UploadFileForm, OperationForm
from .utils.utils import perform_data_operations
from .utils.plot_show_utils import *
from .utils.plot_type_utils import *
import itertools
import random
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import ast
def index(request):
    return render(request, 'DataCleaning/index.html')

# Handling the uploaded file path
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


def data_cleaning(request):
    file_path = request.session.get('file_path', None)

    if file_path:
        # Print some debugging information
        print(f"File Path in data_cleaning: {file_path}")

        # Read file into a pandas DataFrame
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        else:
            pass

        # Get the available columns
        available_columns = list(data.columns)
        #print(f"Available Columns: {available_columns}")

        # Set a limit for the number of rows to display and edit
        row_limit = request.session.get('row_limit', 100)
        data = data.head(row_limit)

        # Convert the DataFrame to a list of dictionaries
        data_list = data.to_dict(orient='records')

        # Instantiate the operation form
        operation_form = OperationForm(available_columns=available_columns)
        # Pass available columns to the template context
        context = {
            'data_list': data_list,
            'file_path': file_path, 
            'available_columns': available_columns, 
            'operation_form': operation_form}

        return render(request, 'DataCleaning/data_cleaning.html', context)
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

# Getting the request
def perform_operation(request):
    file_path = request.session.get('file_path', None)    

    # Dynamically get available columns
    available_columns = get_available_columns(file_path)

    if request.method == 'POST':
        # Pass available columns to the form when initializing it
        operation_form = OperationForm(request.POST, available_columns=available_columns)
        print(f"Form data: {request.POST}")
        print(f"Form errors: {operation_form.errors}")
        if operation_form.is_valid():
            selected_operation = operation_form.cleaned_data['operation']
            selected_columns = operation_form.cleaned_data.get('column_name', [])

            # Print debug information
            print(f"Performing operation: {selected_operation} on columns: {selected_columns}")

            # Perform data operations using the new function
            perform_data_operations(file_path, selected_operation, selected_columns)

    # Redirect back to the data cleaning page after performing the operation
    return redirect('data_cleaning')

# Define the get_available_columns function
def get_available_columns(file_path):
    # Implement logic to dynamically get available columns from the file
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        print("Different file format")    
    # Dynamically get available columns
    available_columns = list(data.columns)
    print(f"Available Columns: {available_columns}")
    return available_columns

# Function to generate all possible combinations of columns with at least 2 columns
def generate_combinations(available_columns):
    num_columns = len(available_columns)
    
    if num_columns < 2:
        print("There are not enough columns available for visualization.")
        return []
    
    max_columns = min(3, num_columns)  # Set the maximum number of columns for combinations
    
    combinations_2 = []
    combinations_3 = []
    for r in range(2, max_columns + 1):  # Start from 2 for at least 2 columns, up to max_columns
        current_combinations = list(itertools.combinations(available_columns, r))
        if r == 2:
            combinations_2.extend(current_combinations)
        else:
            combinations_3.extend(current_combinations)
    return combinations_2, combinations_3

def visualize_selected_combinations(request):
    file_path = request.session.get('file_path', None)
    
    # Get the available columns
    available_columns = get_available_columns(file_path)
    
    # Generate combinations of 2 and 3 columns separately
    combinations_2, combinations_3 = generate_combinations(available_columns)
    
    # Print or log the combinations to inspect them
    print("Combinations of 2 columns:", combinations_2)
    print("Combinations of 3 columns:", combinations_3)
    
    # Pass combinations to the template context
    context = {
        'combinations_2': combinations_2,
        'combinations_3': combinations_3
    }
    
    # Render the template with the context data
    return render(request, 'DataCleaning/data_visualization.html', context)

def data_visualization(request):
    file_path = request.session.get('file_path', None)
    
    if file_path and file_path.endswith('.csv'):
        # Load CSV data into a DataFrame
        data = pd.read_csv(file_path)
        
        # Get available columns
        available_columns = get_available_columns(file_path)
        
        # Generate combinations of 2 and 3 columns separately
        combinations_2, combinations_3 = generate_combinations(available_columns)
        
        if request.method == 'POST':
            print("POST request received")
            # Check if any combinations are selected
            selected_combinations = request.POST.getlist('selected_combinations')
            print("Selected combinations:", selected_combinations) 
            
            selected_visualizations = []
            for combination_str in selected_combinations:
                # Format the selected combination
                combination = ast.literal_eval(combination_str)
                
                if len(combination) == 2:
                    # Check if all columns in the combination exist in the data
                    if all(column in data.columns for column in combination):
                        plot_type = suggest_plot(combination, data)  # Pass combination as a single argument
                        x_column, y_column = combination
                        # call generate function
                        fig = generate_2dplot(plot_type, data, x_column, y_column)
                        plot_html = fig.to_html(full_html=False)
                        selected_visualizations.append(plot_html)
                    else:
                        # Handle the case where the combination contains columns not in the data
                        return render(request, 'error.html', {'error_message': f'Invalid combination: {combination_str}'})
                elif len(combination) == 3:
                    # Check if all columns in the combination exist in the data
                    if all(column in data.columns for column in combination):
                        plot_type = suggest_plot(combination, data)  # Pass combination as a single argument
                        x_column, y_column, z_column = combination
                        fig = generate_3dplot(plot_type, data, x_column, y_column, z_column)
                        plot_html = fig.to_html(full_html=False)
                        selected_visualizations.append(plot_html)
                    else:
                        # Handle the case where the combination contains columns not in the data
                        return render(request, 'error.html', {'error_message': f'Invalid combination: {combination_str}'})
                else:
                    # Handle the case where the combination has an unexpected length
                    return render(request, 'error.html', {'error_message': f'Invalid combination length: {len(combination)}'})
            
            # Return only the selected combinations, not all possible combinations
            return render(request, 'DataCleaning/data_visualization.html', {'visualizations': selected_visualizations,
                                                                            'combinations_2': combinations_2,
                                                                            'combinations_3': combinations_3})

        else:
            # Generate random combinations for initial display
            max_combinations_2 = min(4, len(combinations_2))
            max_combinations_3 = min(4, len(combinations_3))
            
            if len(combinations_2) > max_combinations_2:
                combinations_2 = random.sample(combinations_2, max_combinations_2)
            if len(combinations_3) > max_combinations_3:
                combinations_3 = random.sample(combinations_3, max_combinations_3)
            
            visualizations = []
            for combination in combinations_2:
                x_column, y_column = combination
                plot_type = suggest_plot(combination, data)
                fig = generate_2dplot(plot_type, data, x_column, y_column)
                plot_html = fig.to_html(full_html=False)
                visualizations.append(plot_html)
            
            for combination in combinations_3:
                x_column, y_column, z_column = combination
                plot_type = suggest_plot(combination, data)
                fig = generate_3dplot(plot_type, data, x_column, y_column, z_column)
                plot_html = fig.to_html(full_html=False)
                visualizations.append(plot_html)
            
            return render(request, 'DataCleaning/data_visualization.html', {'visualizations': visualizations,
                                                                            'combinations_2': combinations_2,
                                                                            'combinations_3': combinations_3})
