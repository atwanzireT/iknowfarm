from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import User
from django.urls import reverse_lazy
from .forms import EditUserForm

# Create your views here.
def login(request):
    return render(request, 'login.html', {})

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')

def Profile(request):
    return render(request, 'profile.html', {})

class UserEditView(generic.CreateView):
	form_class = EditUserForm
	template_name = 'edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user