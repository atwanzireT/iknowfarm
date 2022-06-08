from django.urls import path
from . import views

urlpatterns = [
    path('crop_manual',  views.crop_manual, name="crop_manual"),
]