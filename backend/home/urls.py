from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('crops/', CropsListView.as_view(), name="crops"),
    path('livestock/', LiveStockListView.as_view(), name="livestock"),
    path('crop/<int:pk>/', UpdateCropView.as_view(), name="updateCrops"),

]