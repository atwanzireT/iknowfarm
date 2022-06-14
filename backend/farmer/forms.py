from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class FarmerFileForm(forms.ModelForm):
    class Meta:
        model = FarmerFile
        fields = ('title','file')
class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ('name','age', 'expiry', 'status', 'gender', 'farmer_type',  'recommender', 'phonenumber',  'village', 'pin')

class FarmerGroupForm(forms.ModelForm):
    class Meta:
        model = FarmerGroup
        fields = ('name', 'group_type', 'male_farmers', 'female_farmers',  'recommender', 'phonenumber',  'village', 'pin')

class ExtensionWorkerForm(forms.ModelForm):
    class Meta:
        model = ExGroupWorkers
        fields = ('group', 'district', 'name', 'gender',  'designation', 'telephone_number',  'operation_area', 'module')