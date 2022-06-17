from django import forms
from .models import *


class AddVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title','english', 'arabic', 'lugbara', 'cropid', 'livestockid')	

