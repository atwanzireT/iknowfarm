from django import views
from .views import  CropVideoUploads,  LivestockVideoUploads, VideoUploads, AddVideoView
from .models import *
from django.urls import path


urlpatterns = [
    path('crop_videos/', CropVideoUploads, name="CropVideo"),
    path('livestock_videos/', LivestockVideoUploads, name="LivestockVideo"),
    path('videos/', VideoUploads, name="videos"),
    path('addVideo/', AddVideoView.as_view(), name="addVideo"),
]