# forms.py
from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'metadata']

class OperationForm(forms.Form):
    operation = forms.CharField()
    column_name = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple, required=False)

    def __init__(self, *args, available_columns=None, **kwargs):
        super(OperationForm, self).__init__(*args, **kwargs)

        # Populate the choices for the column_name field
        self.fields['column_name'].choices = [(col, col) for col in available_columns] if available_columns else []