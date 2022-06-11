from django import views
from farmer.views import farmer_groups, district, UpdateFarmerView, AddFarmerView, farmer
from .models import *
from django.urls import path


urlpatterns = [
    path("", farmer, name = "farmers"),
    path("groups/", farmer_groups, name = "farmer_groups"),
    path("districts/", district, name = "district"),
    path('updatefarmer/<int:pk>/', UpdateFarmerView.as_view(), name="updateFarmer"),
    path('addfarmer/', AddFarmerView.as_view(), name="addFarmer"),
]