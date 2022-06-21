from farmer.views import *
from .models import *
from django.urls import path
from rest_framework import routers


urlpatterns = [
    path("", farmer, name = "farmers"),
    path("extension_workers/", exension_workers, name = "extension_farmers"),
    path("csv/", farmer_csv, name = "farmers_csv"),
    path("csvgroup/", farmerGroup_csv, name = "farmersgroup_csv"),
    path("groups/", farmer_groups, name = "farmer_groups"),
    path("acc_mgt/", account_management, name = "acc_mgt"),
    # path("districts/", district, name = "district"),
    path('updatefarmer/<int:pk>/', UpdateFarmerView.as_view(), name="updateFarmer"),
    path('addfarmer/', AddFarmerView.as_view(), name="addFarmer"),
    path('add_extension_worker/', AddExtensionWorkerView.as_view(), name="add_extension_worker"),
    path('update_extension_worker/<int:pk>/', UpdateExtensionWorkerView.as_view(), name="updateExtensionWorker"),
    path('addfile/', AddFileView.as_view(), name="addFile"),
    path('deletefarmer/<int:id>/', delete_farmer, name="DeleteFarmer"),
    path('delete_extension_worker/<int:id>/', delete_extension_worker, name="DeleteExtensionWorker"),
    path('deletefarmer_group/<int:id>/', delete_farmer_group, name="DeleteFarmerGroup"),
    path('updatefarmer_group/<int:pk>/', UpdateFarmerGroupView.as_view(), name="updateFarmerGroup"),
    path('addfarmer_group/', AddFarmerGroupView.as_view(), name="addFarmerGroup"),
    path('managefarmer_group/<int:pk>/', ManageFarmerGroupView.as_view(), name="manageFarmerGroup"),
    path('managefarmer/<int:pk>/', ManageFarmerView.as_view(), name="manageFarmer"),

    # Django rest framework routes
    path("api/", FarmerList.as_view(), name="farmer_api"),
    path("groups/api/", FarmerGroupList.as_view(), name="farmer_group_api"),

]