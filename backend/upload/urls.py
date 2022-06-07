from django import views
from .views import CSVupload, VideoUploads
from .models import *
from django.urls import path


urlpatterns = [
    path('data/', CSVupload, name="uploadCsv"),
    path('videos/', VideoUploads, name="uploadVideo"),
]