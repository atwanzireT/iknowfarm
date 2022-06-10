from django.shortcuts import render
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.
def district(request):
    villages = Village.objects.all()
    dic = {
        'villages':villages,
    }
    return render(request, 'districts.html', dic)


def farmer_groups(request):
    farmer_groups = Farmer.objects.filter(registrationtype=2)
    dic = {
        'farmer_groups':farmer_groups,
    }
    return render(request, 'farmergroups.html', dic)
class FarmersListView(LoginRequiredMixin, generic.ListView):
    model = Farmer
    template_name = "farmer_list.html"
    context_object_name= 'farmers'
    login_url = '/profile/login/'

# class UpdateFarmerView(LoginRequiredMixin, generic.UpdateView):
#     model = SingleFarmer
#     template_name = 'editFarmer.html'
#     form_class = FarmerForm
#     login_url = '/profile/login/'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['farmers'] = SingleFarmer.objects.all()
#         return context

# class AddFarmerView(LoginRequiredMixin, generic.CreateView):
#     model = SingleFarmer
#     template_name = 'addFarmer.html'
#     form_class = FarmerForm
#     login_url = '/profile/login/'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['farmers'] = SingleFarmer.objects.all()
#         return context

