from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib import messages
  
# Create your views here.
def feedback(request):
    dic= {}
    return render(request, 'feeds.html', dic)