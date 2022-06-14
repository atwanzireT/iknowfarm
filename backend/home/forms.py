from dataclasses import field
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ('english','arabic', 'lugbara', 'image')


class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ('english','arabic', 'lugbara', 'image')


class CropTranslationForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ('arabic', 'lugbara')

class LivestockTranslationForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ('arabic', 'lugbara')


# class SignupForm(UserCreationForm):
#     GENDER_CHOICES = [
#         ('M', "Male"),
#         ('F', "Female")
#     ]
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length = 50)
#     last_name = forms.CharField(max_length = 50)
#     telephone = forms.CharField(max_length = 50)
#     gender = forms.ChoiceField(choices=GENDER_CHOICES)
#     physical_address = forms.CharField(max_length = 50)

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')