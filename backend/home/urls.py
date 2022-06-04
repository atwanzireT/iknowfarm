from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('crops/', CropsListView.as_view(), name="crops"),
    path('livestock/', LiveStockListView.as_view(), name="livestock"),
    path('updatecrop/<int:pk>/', UpdateCropView.as_view(), name="updateCrops"),
    path('addcrop/', AddCropView.as_view(), name="addCrops"),
]