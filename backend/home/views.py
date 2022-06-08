from django.shortcuts import render
from .models import *
from farmer.models import Farmers
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Crops, Livestock
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
# from .forms import CropForm, CropTranslationForm, LivestockForm, LivestockTranslationForm
from django.urls import reverse

# Create your views here.
@login_required(login_url='/profile/login/')
def index(request):
    # app_users = UserProfile.objects.filter(app_user = 'T').count()
    male_farmers = Farmers.objects.filter(malefarmers__isnull=False).count()
    female_farmers = Farmers.objects.filter(femalefarmers__isnull=False).count()
    farmers = Farmers.objects.filter(registrationtype = 0).count()
    # unregistered_users = UserProfile.objects.filter(registered = 'T').count()

    dic = {
        # 'app_users':app_users,
        'male_farmers':male_farmers,
        'female_farmers':female_farmers,
        'farmers':farmers,
        # 'unregistered_users':unregistered_users,
    }
    return render(request, 'index.html', dic)

@login_required(login_url='/profile/login/')
def crops(request):
    crop_translations = Translations.objects.filter(type = 'Crop')
    dic = {
        'crop_translations':crop_translations,
    }
    return render(request, 'crop_list.html', dic)

@login_required(login_url='/profile/login/')
def livestock(request):
    livestock_translations = Translations.objects.filter(type = 'liv')
    dic = {
        'livestock_translations':livestock_translations,
    }
    return render(request, 'livestock_list.html', dic)


# class UpdateCropView(LoginRequiredMixin, generic.UpdateView):
#     model = Crop
#     template_name = 'editCrop.html'
#     form_class = CropForm
#     login_url = '/profile/login/'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['crops'] = Crop.objects.all()
#         return context

# class AddCropView(LoginRequiredMixin, generic.CreateView):
#     model = Crop
#     template_name = 'addCrop.html'
#     form_class = CropForm
#     login_url = '/profile/login/'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['crops'] = Crop.objects.all()
#         return context

# class UpdateLiveStockView(LoginRequiredMixin, generic.UpdateView):
#     model = Livestock
#     template_name = 'editLivestock.html'
#     form_class = LivestockForm
#     login_url = '/profile/login/'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['livestock'] = Livestock.objects.all()
#         return context

#     def get_success_url(self):
#         return reverse('addLiveStock')

# class AddLiveStockView(LoginRequiredMixin, generic.CreateView):
#     model = Livestock
#     template_name = 'addlivestock.html'
#     form_class = LivestockForm
#     login_url = '/profile/login/'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['crops'] = Livestock.objects.all()
#         return context

#     def get_success_url(self):
#         return reverse('addLiveStock')


# # Translations Views
# class CropsTranslationListView(LoginRequiredMixin, generic.ListView):
#     model = Crop
#     template_name = "cropTrans_list.html"
#     context_object_name= 'crops'
#     login_url = '/profile/login/'

# class LiveStockTranslationListView(LoginRequiredMixin, generic.ListView):
#     model = Livestock
#     template_name = "livestockTrans_list.html"
#     context_object_name= 'livestock'
#     login_url = '/profile/login/'

# class UpdateLiveStockTranslationView(LoginRequiredMixin, generic.UpdateView):
#     model = Livestock
#     template_name = 'editLivestockTranslation.html'
#     form_class = LivestockTranslationForm
#     login_url = '/profile/login/'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['livestock'] = Livestock.objects.all()
#         return context

#     def get_success_url(self):
#         return reverse('addLiveStock')

# class UpdateCropTranslationView(LoginRequiredMixin, generic.UpdateView):
#     model = Crop
#     template_name = 'editCropTranslation.html'
#     form_class = CropTranslationForm
#     login_url = '/profile/login/'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['crops'] = Crop.objects.all()
#         return context