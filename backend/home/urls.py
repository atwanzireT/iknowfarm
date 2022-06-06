from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('crops/', CropsListView.as_view(), name="crops"),
    path('livestock/', LiveStockListView.as_view(), name="livestock"),
    path('translation/crops/', CropsTranslationListView.as_view(), name="crops_translations"),
    path('translation/livestock/', LiveStockTranslationListView.as_view(), name="livestock_translations"),
    path('updatecrop/<int:pk>/', UpdateCropView.as_view(), name="updateCrops"),
    path('addcrop/', AddCropView.as_view(), name="addCrops"),
    path('updatelivestock/<int:pk>/', UpdateLiveStockView.as_view(), name="updateLivestock"),
    path('addlivestock/', AddLiveStockView.as_view(), name="addLiveStock"),
]