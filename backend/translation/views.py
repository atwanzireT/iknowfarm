from django.shortcuts import render
from .models import *


# Create your views here.
def crop_manual(request):
    tomato = Translations.objects.filter(key = "xJKsWphSjigu")
    dic= {
        'tomato':tomato,
    }
    return render(request, 'crop_manual.html', dic)