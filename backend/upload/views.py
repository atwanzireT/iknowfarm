from django.shortcuts import render
from .models import VideoUpload
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .form import AddVideoForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
@login_required(login_url='/profile/login/')
def CSVupload(request):
    return render(request, 'farmercsv.html', {})

@login_required(login_url='/profile/login/')
def CropVideoUploads(request):
    crop_videos = VideoUpload.objects.filter(crop_id__isnull=False)

    dic = {
        'crop_videos': crop_videos,	
    }
    return render(request, "Cropvideo.html", dic)

@login_required(login_url='/profile/login/')
def LivestockVideoUploads(request):
    livestock_videos = VideoUpload.objects.filter(Livestock_id__isnull=False)
    dic = {
        'livestock_videos': livestock_videos,
    }
    return render(request, "Livestockvideo.html", dic)

@login_required(login_url='/profile/login/')
def VideoUploads(request):
    videos = VideoUpload.objects.all()
    dic = {
        'videos': videos,
    }
    return render(request, "video.html", dic)
    
class AddVideoView(LoginRequiredMixin, generic.CreateView):
    model = VideoUpload
    template_name = 'addVideo.html'
    form_class = AddVideoForm
    login_url = '/profile/login/'

    def get_success_url(self):
        return reverse('addLiveStock')