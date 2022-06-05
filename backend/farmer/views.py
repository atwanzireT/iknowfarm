from django.shortcuts import render
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.
class FarmersListView(LoginRequiredMixin, generic.ListView):
    model = SingleFarmer
    template_name = "farmer_list.html"
    context_object_name= 'farmers'
    login_url = '/profile/login/'