from django.shortcuts import render
from .models import VideoUpload
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .form import AddVideoForm

# Create your views here.
def CSVupload(request):
    return render(request, 'farmercsv.html', {})

def VideoUploads(request):
    crop_videos = VideoUpload.objects.filter(crop_id__isnull=False)
    livestock_videos = VideoUpload.objects.filter(Livestock_id__isnull=False)
    videos = VideoUpload.objects.all()
    dic = {
        'crop_videos': crop_videos,	
        'livestock_videos': livestock_videos,
        'videos': videos
    }
    return render(request, "video.html", dic)

class AddVideoView(LoginRequiredMixin, generic.CreateView):
    model = VideoUploads
    template_name = 'addVideo.html'
    form_class = AddVideoForm
    login_url = '/profile/login/'