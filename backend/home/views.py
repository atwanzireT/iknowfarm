from tokenize import group
from django.shortcuts import render
from .models import Crop, Livestock, UnregistredUser
from farmer.models import Farmer, Village
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CropForm, CropTranslationForm, LivestockForm, LivestockTranslationForm
from django.urls import reverse, reverse_lazy
from translation.models import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/profile/login/')
def index(request):
    male_farmers = Farmer.objects.filter(gender = 'male').count()
    female_farmers = Farmer.objects.filter(gender = 'female').count()
    farmers = Farmer.objects.filter(group__isnull = True).count()
    unregistered_users = UnregistredUser.objects.all().count()
    app_users = User.objects.all().count()
    app_installations = farmers + unregistered_users + app_users

    dic = {
        'male_farmers':male_farmers,
        'female_farmers':female_farmers,
        'farmers':farmers,
        'unregistered_users':unregistered_users,
        'app_users':app_users,
        'app_installations':app_installations,
    }
    return render(request, 'index.html', dic)

@login_required(login_url='/profile/login/')
def districts(request):
    districts = Village.objects.all()

    paginator = Paginator(districts, 20)
    page = request.GET.get('page')
    districts = paginator.get_page(page)
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
        context['crop'] = Crop.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse_lazy('crops')

class AddCropView(LoginRequiredMixin, generic.CreateView):
    model = Crop
    template_name = 'addCrop.html'
    form_class = CropForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['crop'] = Crop.objects.all()[:10]
        return context

    def get_success_url(self):
        return reverse_lazy('crops')


class UpdateLiveStockView(LoginRequiredMixin, generic.UpdateView):
    model = Livestock
    template_name = 'editLivestock.html'
    form_class = LivestockForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['livestock'] = Livestock.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse_lazy('livestock')

class AddLiveStockView(LoginRequiredMixin, generic.CreateView):
    model = Livestock
    template_name = 'addlivestock.html'
    form_class = LivestockForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['livestock'] = Livestock.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse_lazy('livestock')


# Translations Views
@login_required(login_url='/profile/login/')
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

@login_required(login_url='/profile/login/')
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
        context['livestock'] = Livestock.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse_lazy('livestock_translations')

class UpdateCropTranslationView(LoginRequiredMixin, generic.UpdateView):
    model = Crop
    template_name = 'editCropTranslation.html'
    form_class = CropTranslationForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['crops'] = Crop.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse_lazy('crops_translations')