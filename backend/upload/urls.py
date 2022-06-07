from django import views
from farmer.views import CSVupload
from .models import *
from django.urls import path


urlpatterns = [
    path('upload/data/', CSVupload, name="uploadCsv"),
]