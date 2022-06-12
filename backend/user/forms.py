from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from django import forms

class EditUserForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
