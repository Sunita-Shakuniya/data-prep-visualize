import pandas as pd
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.urls import reverse
from DataCleaning.models import UploadedFile

from DataCleaning.forms import UploadFileForm


def index(request):
    return render(request, 'DataCleaning/index.html')

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

#Testing with hard coded file path
def data_processing(request):
    print(request.session.items())

    # Read CSV file into a pandas DataFrame
    csv_path = 'C:/Users/sunit/Django_React/Data_Project/DataScience/media/uploads/data_science_salaries.csv'
    row_limit = request.session.get('row_limit',100)
    data = pd.read_csv(csv_path)

    # Set a limit for the number of rows to display and edit
    data = data.head(row_limit)

    
    # Convert the DataFrame to a list of dictionaries
    data_list = data.to_dict(orient='records')

    return render(request, 'DataCleaning/data_processing.html', {'data_list': data_list})

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

# Visualization part
def data_visualization(request):
    # Add your logic for the data visualization page
    return render(request, 'DataCleaning/data_visualization.html')    





