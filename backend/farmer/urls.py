from django import views
from farmer.views import FarmersListView, AddFarmerView, UpdateFarmerView
from .models import *
from django.urls import path


urlpatterns = [
    path("", FarmersListView.as_view(), name = "farmers"),
    path('updatefarmer/<int:pk>/', UpdateFarmerView.as_view(), name="updateFarmer"),
    path('addfarmer/', AddFarmerView.as_view(), name="addFarmer"),
]