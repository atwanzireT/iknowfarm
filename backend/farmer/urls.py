from farmer.views import *
from .models import *
from django.urls import path


urlpatterns = [
    path("", farmer, name = "farmers"),
    path("csv/", farmer_csv, name = "farmers_csv"),
    path("groups/", farmer_groups, name = "farmer_groups"),
    path("districts/", district, name = "district"),
    path('updatefarmer/<int:pk>/', UpdateFarmerView.as_view(), name="updateFarmer"),
    path('addfarmer/', AddFarmerView.as_view(), name="addFarmer"),
]