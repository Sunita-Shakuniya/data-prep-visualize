import os
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse, HttpResponseBadRequest

def index(request):
    return render(request, 'DataCleaning/index.html')
#Not working Let see later
def handle_uploaded_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_path = default_storage.save('uploads/' + uploaded_file.name, uploaded_file)
        
        # Your additional file handling logic here
        # For example, you can process the file contents or store additional metadata
        
        return JsonResponse({'message': 'File uploaded successfully', 'file_path': file_path})
    else:
        return JsonResponse({'error': 'Invalid request'})
    
def data_cleaning(request):
    # Add your logic for the data cleaning page
    return render(request, 'DataCleaning/data_cleaning.html')

def data_visualization(request):
    # Add your logic for the data visualization page
    return render(request, 'DataCleaning/data_visualization.html')    