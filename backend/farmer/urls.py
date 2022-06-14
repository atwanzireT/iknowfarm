from farmer.views import *
from .models import *
from django.urls import path


urlpatterns = [
    path("", farmer, name = "farmers"),
    path("extension_workers/", exension_workers, name = "extension_farmers"),
    path("csv/", farmer_csv, name = "farmers_csv"),
    path("groups/", farmer_groups, name = "farmer_groups"),
    path("districts/", district, name = "district"),
    path('updatefarmer/<int:pk>/', UpdateFarmerView.as_view(), name="updateFarmer"),
    path('addfarmer/', AddFarmerView.as_view(), name="addFarmer"),
    path('addfile/', AddFileView.as_view(), name="addFile"),
    path('deletefarmer/<int:pk>/', FarmerDeleteView.as_view(), name="DeleteFarmer"),

]