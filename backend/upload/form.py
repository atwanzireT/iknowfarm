from django import forms
from .models import *


class AddVideoForm(forms.ModelForm):
    class Meta:
        model = VideoUpload
        fields = ('title','english_video', 'arabic_video', 'lugba_video', 'crop_id', 'Livestock_id')	

class AddCsvForm(forms.ModelForm):
    class Meta:
        model = CsvFile
        fields = ('file', )	
