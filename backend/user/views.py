from ast import Return
from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash

# Create your views here.
def login(request):
    return render(request, 'login.html', {})

