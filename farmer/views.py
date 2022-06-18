from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from farmer.serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
import csv



# Create your views here.
@login_required(login_url='/profile/login/')
def farmer_groups(request):
    farmer_groups = FarmerGroup.objects.all()

    search = request.GET.get("search")
    if search != "" and search is not None:
        farmer_groups = FarmerGroup.objects.filter(name__icontains=search)[:20]
        return render(request, "searchedFarmer.html", {'farmer_groups':farmer_groups})

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
        context['farmer_groups'] = FarmerGroup.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse('/farmers')


class AddFarmerGroupView(LoginRequiredMixin, generic.CreateView):
    model = FarmerGroup
    template_name = 'addFarmerGroup.html'
    form_class = FarmerGroupForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['farmer_groups'] = FarmerGroup.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse('farmer_groups')

class UpdateFarmerGroupView(LoginRequiredMixin, generic.UpdateView):
    model = FarmerGroup
    template_name = 'editFarmerGroup.html'
    form_class = FarmerGroupForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['farmer_groups'] = FarmerGroup.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse('farmer_groups')

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

@login_required(login_url='/profile/login/')
def farmer_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="farmers.csv"'

    # Create CSV writer
    writer = csv.writer(response)
    farmers = Farmer.objects.all()
    
    # Add column headers to csv file
    writer.writerow(['name','age', 'gender', 'phonenumber', 'status',   'recommender',   'pin', 'expiry', 'farmer_type', 'createdat', 'updatedat', ])

    for farmer in farmers:
        writer.writerow([farmer.name, farmer.age, farmer.gender, farmer.phonenumber, farmer.status,  farmer.recommender,  farmer.pin, farmer.expiry, farmer.createdat, farmer.updatedat])
       
    
    return response

@login_required(login_url='/profile/login/')
def farmerGroup_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="farmerGroup.csv"'

    # Create CSV writer
    writer = csv.writer(response)
    farmers = FarmerGroup.objects.all()
    
    # Add column headers to csv file
    writer.writerow(['name', 'group_type', 'male_farmers', 'female_farmers',  'recommender', 'phonenumber',  'village', 'createdat', 'updatedat', ])

    for farmer in farmers:
        writer.writerow([farmer.name, farmer.group_type, farmer.male_farmers, farmer.female_farmers, farmer.recommender,  farmer.phonenumber,  farmer.pin, farmer.createdat, farmer.updatedat])
       
    
    return response

class AddFileView(LoginRequiredMixin, generic.CreateView):
    model = FarmerFile
    template_name = 'addfile.html'
    form_class = FarmerFileForm
    login_url = '/profile/login/'

    def get_success_url(self):
        return reverse('videos')

@login_required(login_url='/profile/login/')
def delete_farmer(request,id):
    Farmer.objects.filter(id=id).delete()
    messages.success(request, "Farmer Deleted.")
    return HttpResponseRedirect("/farmers/")

@login_required(login_url='/profile/login/')
def delete_farmer_group(request,id):
    FarmerGroup.objects.filter(id=id).delete()
    messages.success(request, "Farmer Group Deleted.")
    return HttpResponseRedirect("/farmers/groups/")

# Extension workers views 
@login_required(login_url='/profile/login/')
def exension_workers(request):
    ex_workers = ExGroupWorkers.objects.all().order_by('name')

    search = request.GET.get("search")
    if search != "" and search is not None:
        ex_workers = ExGroupWorkers.objects.filter(name__icontains=search)[:20]
        return render(request, "searchedExworker.html", {'ex_workers':ex_workers})

    paginator = Paginator(ex_workers, 5)
    page = request.GET.get('page')
    ex_workers = paginator.get_page(page)
    dic = {
        'ex_workers':ex_workers,
    }
    return render(request, 'ex_workers.html', dic)

class AddExtensionWorkerView(LoginRequiredMixin, generic.CreateView):
    model = ExGroupWorkers
    template_name = 'addextensionWorker.html'
    form_class = ExtensionWorkerForm
    login_url = '/profile/login/'

    def get_success_url(self):
        return reverse('extension_workers')

class UpdateExtensionWorkerView(LoginRequiredMixin, generic.UpdateView):
    model = ExGroupWorkers
    template_name = 'UpdateExtensionWorker.html'
    form_class = ExtensionWorkerForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['ex_workers'] = ExGroupWorkers.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse_lazy('extension_workers')

@login_required(login_url='/profile/login/')
def delete_extension_worker(request,id):
    ExGroupWorkers.objects.filter(id=id).delete()
    messages.success(request, "Extension Worker Deleted.")
    return HttpResponseRedirect("/farmers/extension_workers/")

# Account management
def account_management(request):
    farmers = Farmer.objects.all()[:10]
    farmer_group = FarmerGroup.objects.all()[:10]

    search = request.GET.get("search")
    if search != "" and search is not None:
        farmers = Farmer.objects.filter(name__icontains=search)[:20]
        farmer_group = FarmerGroup.objects.filter(name__icontains=search)[:20]
        return render(request, "searchedmgt.html", {'farmers':farmers, 'farmer_group': farmer_group})

    dic = {
        'farmers':farmers,
        'farmer_group':farmer_group,
    }
    return render(request, "accountmanagemnent.html", dic)

class ManageFarmerGroupView(LoginRequiredMixin, generic.UpdateView):
    model = FarmerGroup
    template_name = 'ManageFarmer.html'
    form_class = ManageGroupForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['farmer_groups'] = FarmerGroup.objects.all().order_by('?')[:10]
        context['farmers'] = Farmer.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse('acc_mgt')

class ManageFarmerView(LoginRequiredMixin, generic.UpdateView):
    model = Farmer
    template_name = 'ManageFarmer.html'
    form_class = ManageFarmerForm
    login_url = '/profile/login/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['farmer_groups'] = FarmerGroup.objects.all().order_by('?')[:10]
        context['farmers'] = Farmer.objects.all().order_by('?')[:10]
        return context

    def get_success_url(self):
        return reverse('acc_mgt')


"""
    Creating Serializer Views
"""

class FarmerList(generics.ListCreateAPIView):
    """
        Allows viewing all Farmers
    """
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class FarmerGroupList(generics.ListCreateAPIView):
    """
        Allows viewing and creating Farmer Groups
    """
    queryset = FarmerGroup.objects.all()
    serializer_class = FarmerGroupSerializers