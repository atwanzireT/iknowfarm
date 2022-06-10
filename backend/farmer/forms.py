from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ('name','date_of_birth', 'expiry', 'status', 'gender',  'recommender', 'phonenumber',  'villages')

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Name'}),
        'Date_of_Birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Arabic'}),
        'expiry': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Lugbar'}),
    }