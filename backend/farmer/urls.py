from farmer.views import *
from .models import *
from django.urls import path


urlpatterns = [
    path("", farmer, name = "farmers"),
    path("extension_workers/", exension_workers, name = "extension_farmers"),
    path("csv/", farmer_csv, name = "farmers_csv"),
    path("groups/", farmer_groups, name = "farmer_groups"),
    # path("districts/", district, name = "district"),
    path('updatefarmer/<int:pk>/', UpdateFarmerView.as_view(), name="updateFarmer"),
    path('addfarmer/', AddFarmerView.as_view(), name="addFarmer"),
    path('add_extension_worker/', AddExtensionWorkerView.as_view(), name="add_extension_worker"),
    path('update_extension_worker/<int:pk>/', UpdateExtensionWorkerView.as_view(), name="updateExtensionWorker"),
    path('addfile/', AddFileView.as_view(), name="addFile"),
    path('deletefarmer/<int:id>/', delete_farmer, name="DeleteFarmer"),
    path('delete_extension_worker/<int:id>/', delete_extension_worker, name="DeleteExtensionWorker"),
    path('deletefarmer_group/<int:id>/', delete_farmer_group, name="DeleteFarmerGroup"),


]