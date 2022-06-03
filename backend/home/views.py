from django.shortcuts import render
from user.models import UserProfile
from farmer.models import FarmerGroup, SingleFarmer
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Crop, Livestock
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/profile/login/')
def index(request):
    app_users = UserProfile.objects.filter(app_user = 'T').count()
    male_farmers = SingleFarmer.objects.filter(gender = 'M').count()
    female_farmers = SingleFarmer.objects.filter(gender = 'F').count()
    farmers = SingleFarmer.objects.all().count()
    unregistered_users = UserProfile.objects.filter(registered = 'T').count()

    dic = {
        'app_users':app_users,
        'male_farmers':male_farmers,
        'female_farmers':female_farmers,
        'farmers':farmers,
        'unregistered_users':unregistered_users,
    }
    return render(request, 'index.html', dic)

# @login_required(login_url='/profile/login/')
class CropsListView(LoginRequiredMixin, generic.ListView):
    model = Crop
    template_name = "crop_list.html"
    context_object_name= 'crops'
    login_url = '/profile/login/'

class LiveStockListView(LoginRequiredMixin, generic.ListView):
    model = Livestock
    template_name = "livestock_list.html"
    context_object_name= 'livestock'
    login_url = '/profile/login/'
