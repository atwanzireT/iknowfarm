from django import views
from .views import  CropVideoUploads,  LivestockVideoUploads, VideoUploads
from .models import *
from django.urls import path


urlpatterns = [
    path('crop_videos/', CropVideoUploads, name="CropVideo"),
    path('livestock_videos/', LivestockVideoUploads, name="LivestockVideo"),
    path('videos/', VideoUploads, name="video"),
    # path('addVideo/', AddVideoView.as_view(), name="addVideo"),
]