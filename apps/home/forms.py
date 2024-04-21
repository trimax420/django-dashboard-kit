from django import forms
from .models import UploadFile
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('excel_file','laz_file','obj_file','kml_file' )