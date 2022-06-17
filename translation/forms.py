from django import forms
from .models import *


class EnglishManualForm(forms.ModelForm):
    class Meta:
        model = Manual
        fields = ('english',)

class LugbaraManualForm(forms.ModelForm):
    class Meta:
        model = Manual
        fields = ('lugbara',)

class ArabicManualForm(forms.ModelForm):
    class Meta:
        model = Manual
        fields = ('arabic',)