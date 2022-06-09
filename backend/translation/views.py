from django.shortcuts import render
from .models import *


# Create your views here.
def crop_manual(request):
    # tomato = CropManuals.objects.all()
    tomato = Translations.objects.filter(type='MAN')
    dic= {
        'tomato':tomato,
    }
    return render(request, 'crop_manual.html', dic)