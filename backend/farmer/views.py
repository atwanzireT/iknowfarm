import imp
from django.shortcuts import render
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import *
from django.core.paginator import Paginator
from django.http import FileResponse, HttpResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, landscape


# Create your views here.
def district(request):
    villages = Village.objects.all()
    dic = {
        'villages':villages,
    }
    return render(request, 'districts.html', dic)


def farmer_groups(request):
    farmer_groups = FarmerGroup.objects.all()

    paginator = Paginator(farmer_groups, 5)
    page = request.GET.get('page')
    farmer_groups = paginator.get_page(page)
    dic = {
        'farmer_groups':farmer_groups,
    }
    return render(request, 'farmergroups.html', dic)

def farmer(request):
    farmers = Farmer.objects.all()

    paginator = Paginator(farmers, 5)
    page = request.GET.get('page')
    farmers = paginator.get_page(page)
    dic = {
        'farmers':farmers,
    }
    return render(request, 'farmer_list.html', dic)

class UpdateFarmerView(LoginRequiredMixin, generic.UpdateView):
    model = Farmer
    template_name = 'editFarmer.html'
    form_class = FarmerForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['farmers'] = Farmer.objects.all()
        return context

class AddFarmerView(LoginRequiredMixin, generic.CreateView):
    model = Farmer
    template_name = 'addFarmer.html'
    form_class = FarmerForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['farmers'] = Farmer.objects.all()
        return context

def farmer_csv(request):
    # return HttpResponse()
    pass

class AddFileView(LoginRequiredMixin, generic.CreateView):
    model = FarmerFile
    template_name = 'addfile.html'
    form_class = FarmerFileForm
    login_url = '/profile/login/'

    def get_success_url(self):
        return reverse('videos')