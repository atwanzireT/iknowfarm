from django import views
from .views import CSVupload, CropVideoUploads, AddVideoView, LivestockVideoUploads, VideoUploads
from .models import *
from django.urls import path


urlpatterns = [
    path('data/', CSVupload, name="uploadCsv"),
    path('crop_videos/', CropVideoUploads, name="CropVideo"),
    path('livestock_videos/', LivestockVideoUploads, name="LivestockVideo"),
    path('videos/', VideoUploads, name="video"),
    path('addVideo/', AddVideoView.as_view(), name="addVideo"),
]