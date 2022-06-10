from django.shortcuts import render
from .models import *
from .forms import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


# Create your views here.
def crop_manual(request):
    tomato = Manual.objects.filter(cropid = 1)
    dic= {
        'tomato':tomato,
    }
    return render(request, 'crop_manual.html', dic)

class UpdateManualView(LoginRequiredMixin, generic.UpdateView):
    model = Manual
    template_name = 'crop_manual_eng_edit.html'
    form_class = EnglishManualForm
    login_url = '/profile/login/'

    def get_success_url(self):
        return reverse('crop_manual')

class EngManualDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manual
    template_name = 'crop_manual_eng.html'
    login_url = '/profile/login/'

class LugbaraManualDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manual
    template_name = 'crop_manual_lugbara.html'
    login_url = '/profile/login/'

class ArabicManualDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manual
    template_name = 'crop_manual_arabic.html'
    login_url = '/profile/login/'

class UpdateArabicManualView(LoginRequiredMixin, generic.UpdateView):
    model = Manual
    template_name = 'crop_manual_arabic_edit.html'
    form_class = ArabicManualForm
    login_url = '/profile/login/'

    def get_success_url(self):
        return reverse('crop_manual')

class UpdateLugbaraManualView(LoginRequiredMixin, generic.UpdateView):
    model = Manual
    template_name = 'crop_manual_lugbara_edit.html'
    form_class = LugbaraManualForm
    login_url = '/profile/login/'

    def get_success_url(self):
        return reverse('crop_manual')

# class AddFarmerView(LoginRequiredMixin, generic.CreateView):
#     model = Manual
#     template_name = 'crop_manual_eng_edit.html'
#     form_class = EnglishManualForm
#     login_url = '/profile/login/'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['farmers'] = Farmer.objects.all()
#         return context