from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ('name','Date_of_Birth', 'expiry', 'status', 'gender',  'recommender', 'phone',  'Village')

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Name'}),
        'Date_of_Birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Arabic'}),
        'expiry': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Lugbar'}),
    }