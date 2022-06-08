from django.shortcuts import render
from .models import Videos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .form import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
@login_required(login_url='/profile/login/')
def CropVideoUploads(request):
    crop_videos = Videos.objects.filter(cropid__isnull=False)

    dic = {
        'crop_videos': crop_videos,	
    }
    return render(request, "Cropvideo.html", dic)

@login_required(login_url='/profile/login/')
def LivestockVideoUploads(request):
    livestock_videos = Videos.objects.filter(livestockid__isnull=False)
    dic = {
        'livestock_videos': livestock_videos,
    }
    return render(request, "Livestockvideo.html", dic)

@login_required(login_url='/profile/login/')
def VideoUploads(request):
    videos = Videos.objects.all()
    dic = {
        'videos': videos,
    }
    return render(request, "video.html", dic)
    
# class AddVideoView(LoginRequiredMixin, generic.CreateView):
#     model = Videos
#     template_name = 'addVideo.html'
#     form_class = AddVideoForm
#     login_url = '/profile/login/'

#     def get_success_url(self):
#         return reverse('addLiveStock')