from tokenize import group
from django.shortcuts import render
from .models import Crop, Livestock, UnregistredUser
from farmer.models import Farmer, Village
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CropForm, CropTranslationForm, LivestockForm, LivestockTranslationForm
from django.urls import reverse
from translation.models import *
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url='/profile/login/')
def index(request):
    male_farmers = Farmer.objects.filter(gender = 'male').count()
    female_farmers = Farmer.objects.filter(gender = 'female').count()
    farmers = Farmer.objects.filter(group__isnull = True).count()
    unregistered_users = UnregistredUser.objects.all().count()

    dic = {
        'male_farmers':male_farmers,
        'female_farmers':female_farmers,
        'farmers':farmers,
        'unregistered_users':unregistered_users,
    }
    return render(request, 'index.html', dic)

@login_required(login_url='/profile/login/')
def districts(request):
    districts = Village.objects.all()
    dic = {
        'districts':districts,
    }
    return render(request, "district.html", dic)

    
@login_required(login_url='/profile/login/')
def crops(request):
    crop = Crop.objects.all()

    # crop Pagnition
    paginator = Paginator(crop, 5)
    page = request.GET.get('page')
    crop = paginator.get_page(page)

    dic = {
        'crop':crop,
    }
    return render(request, 'crop_list.html', dic)

@login_required(login_url='/profile/login/')
def livestock(request):
    livestock = Livestock.objects.all()
    dic = {
        'livestock':livestock,
    }
    return render(request, 'livestock_list.html', dic)


class UpdateCropView(LoginRequiredMixin, generic.UpdateView):
    model = Crop
    template_name = 'editCrop.html'
    form_class = CropForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['crop'] = Crop.objects.all()
        return context

    def get_success_url(self):
        return reverse('crops')

class AddCropView(LoginRequiredMixin, generic.CreateView):
    model = Crop
    template_name = 'addCrop.html'
    form_class = CropForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['crop'] = Crop.objects.all()
        return context

    def get_success_url(self):
        return reverse('crops')


class UpdateLiveStockView(LoginRequiredMixin, generic.UpdateView):
    model = Livestock
    template_name = 'editLivestock.html'
    form_class = LivestockForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['livestock'] = Livestock.objects.all()
        return context

    def get_success_url(self):
        return reverse('liveStock')

class AddLiveStockView(LoginRequiredMixin, generic.CreateView):
    model = Livestock
    template_name = 'addlivestock.html'
    form_class = LivestockForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['livestock'] = Livestock.objects.all()
        return context

    def get_success_url(self):
        return reverse('liveStock')


# Translations Views
def cropTranslation(request):
    crops = Crop.objects.all()

    # crop Pagnition
    paginator = Paginator(crops, 5)
    page = request.GET.get('page')
    crops = paginator.get_page(page)
    dic = {
        'crops': crops,
    }
    return render(request, 'cropTrans_list.html', dic)

def livestockTranslation(request):
    livestock = Livestock.objects.all()

    # crop Pagnition
    paginator = Paginator(livestock, 5)
    page = request.GET.get('page')
    livestock = paginator.get_page(page)
    dic = {
        'livestock': livestock,
    }
    return render(request, 'livestockTrans_list.html', dic)

class UpdateLiveStockTranslationView(LoginRequiredMixin, generic.UpdateView):
    model = Livestock
    template_name = 'editLivestockTranslation.html'
    form_class = LivestockTranslationForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['livestock'] = Livestock.objects.all()
        return context

    def get_success_url(self):
        return reverse('livestock_translations')

class UpdateCropTranslationView(LoginRequiredMixin, generic.UpdateView):
    model = Crop
    template_name = 'editCropTranslation.html'
    form_class = CropTranslationForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['crops'] = Crop.objects.all()
        return context

    def get_success_url(self):
        return reverse('crops_translations')