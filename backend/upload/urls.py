from django import views
from farmer.views import CSVupload, VideoUploads
from .models import *
from django.urls import path


urlpatterns = [
    path('data/', CSVupload, name="uploadCsv"),
    path('video/', VideoUploads, name="uploadVideo"),
]