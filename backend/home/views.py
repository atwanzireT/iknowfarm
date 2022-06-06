from django.shortcuts import render
# from user.models import UserProfile
from farmer.models import FarmerGroup, SingleFarmer
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Crop, Livestock
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .forms import CropForm, LivestockForm
from django.urls import reverse

# Create your views here.
@login_required(login_url='/profile/login/')
def index(request):
    # app_users = UserProfile.objects.filter(app_user = 'T').count()
    male_farmers = SingleFarmer.objects.filter(gender = 'M').count()
    female_farmers = SingleFarmer.objects.filter(gender = 'F').count()
    farmers = SingleFarmer.objects.all().count()
    # unregistered_users = UserProfile.objects.filter(registered = 'T').count()

    dic = {
        # 'app_users':app_users,
        'male_farmers':male_farmers,
        'female_farmers':female_farmers,
        'farmers':farmers,
        # 'unregistered_users':unregistered_users,
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

class UpdateCropView(LoginRequiredMixin, generic.UpdateView):
    model = Crop
    template_name = 'editCrop.html'
    form_class = CropForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['crops'] = Crop.objects.all()
        return context

class AddCropView(LoginRequiredMixin, generic.CreateView):
    model = Crop
    template_name = 'addCrop.html'
    form_class = CropForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['crops'] = Crop.objects.all()
        return context

class UpdateLiveStockView(LoginRequiredMixin, generic.UpdateView):
    model = Crop
    template_name = 'editLivestock.html'
    form_class = LivestockForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['crops'] = Livestock.objects.all()
        return context

    def get_success_url(self):
        return reverse('addLiveStock')

class AddLiveStockView(LoginRequiredMixin, generic.CreateView):
    model = Livestock
    template_name = 'addlivestock.html'
    form_class = LivestockForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['crops'] = Livestock.objects.all()
        return context

    def get_success_url(self):
        return reverse('addLiveStock')


class CropsTranslationListView(LoginRequiredMixin, generic.ListView):
    model = Crop
    template_name = "cropTransTrans_list.html"
    context_object_name= 'crops'
    login_url = '/profile/login/'

class LiveStockTranslationListView(LoginRequiredMixin, generic.ListView):
    model = Livestock
    template_name = "livestock_list.html"
    context_object_name= 'livestock'
    login_url = '/profile/login/'