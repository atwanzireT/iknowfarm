from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ('name','age', 'expiry', 'status', 'gender',  'recommender', 'phonenumber',  'villages')