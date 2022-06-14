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
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy




# Create your views here.
@login_required(login_url='/profile/login/')
def district(request):
    villages = Village.objects.all()
    dic = {
        'villages':villages,
    }
    return render(request, 'districts.html', dic)


@login_required(login_url='/profile/login/')
def farmer_groups(request):
    farmer_groups = FarmerGroup.objects.all()

    paginator = Paginator(farmer_groups, 5)
    page = request.GET.get('page')
    farmer_groups = paginator.get_page(page)
    dic = {
        'farmer_groups':farmer_groups,
    }
    return render(request, 'farmergroups.html', dic)

@login_required(login_url='/profile/login/')
def farmer(request):
    farmers = Farmer.objects.all()

    search = request.GET.get("search")
    if search != "" and search is not None:
        farmers = Farmer.objects.filter(name__icontains=search)[:20]
        return render(request, "search.html", {'farmers':farmers})

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
        context['farmers'] = Farmer.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse('/farmers')

class AddFarmerView(LoginRequiredMixin, generic.CreateView):
    model = Farmer
    template_name = 'addFarmer.html'
    form_class = FarmerForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['farmers'] = Farmer.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse('/farmers/')

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

class FarmerDeleteView(generic.DeleteView):
    model = Farmer
    success_url = reverse_lazy('/farmer/')


def exension_workers(request):
    ex_workers = ExGroupWorkers.objects.all()

    paginator = Paginator(ex_workers, 5)
    page = request.GET.get('page')
    ex_workers = paginator.get_page(page)
    dic = {
        'ex_workers':ex_workers,
    }
    return render(request, 'ex_workers.html', dic)