from django.shortcuts import render
from farmer.models import Farmer
from feedback.models import Feedback
from .models import Video
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .form import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
# from rest_framework import serializers, viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response

# import csv


# # Create your views here.
# fs = FileSystemStorage(location='tmp/')

# class FarmerSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Farmer
#         fields = ('name','age', 'expiry', 'status', 'gender', 'farmer_type',  'recommender', 'phonenumber',  'village', 'pin')

# class FarmerViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing Product.
#     """
#     queryset = Farmer.objects.all()
#     serializer_class = FarmerSerializer

#     @action(detail=False, methods=['POST'])
#     def upload_data(self, request):
#         """Upload data from CSV"""
#         file = request.FILES["file"]

#         content = file.read()  # these are bytes
#         file_content = ContentFile(content)
#         file_name = fs.save(
#             "_tmp.csv", file_content
#         )
#         tmp_file = fs.path(file_name)

#         csv_file = open(tmp_file, errors="ignore")
#         reader = csv.reader(csv_file)
#         next(reader)

#         return Response("Successfully upload the data")

@login_required(login_url='/profile/login/')
def CropVideoUploads(request):
    crop_videos = Video.objects.filter(cropid__isnull=False)

    dic = {
        'crop_videos': crop_videos,	
    }
    return render(request, "Cropvideo.html", dic)

@login_required(login_url='/profile/login/')
def LivestockVideoUploads(request):
    livestock_videos = Video.objects.filter(livestockid__isnull=False)
    dic = {
        'livestock_videos': livestock_videos,
    }
    return render(request, "Livestockvideo.html", dic)

@login_required(login_url='/profile/login/')
def VideoUploads(request):
    videos = Video.objects.all()
    dic = {
        'videos': videos,
    }
    return render(request, "video.html", dic)
    
class AddVideoView(LoginRequiredMixin, generic.CreateView):
    model = Video
    template_name = 'addVideo.html'
    form_class = AddVideoForm
    login_url = '/profile/login/'

    def get_success_url(self):
        return reverse('videos')

