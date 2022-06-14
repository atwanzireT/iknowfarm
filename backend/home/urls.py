from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('districts/', districts, name='districts'),
    path('crops/', crops, name="crops"),
    path('livestock/', livestock, name="livestock"),
    path('translation/crops/', cropTranslation, name="crops_translations"),
    path('translation/livestock/', livestockTranslation, name="livestock_translations"),
    path('updatecrop/<int:pk>/', UpdateCropView.as_view(), name="updateCrops"),
    path('addcrop/', AddCropView.as_view(), name="addCrops"),
    path('updatelivestock/<int:pk>/', UpdateLiveStockView.as_view(), name="updateLivestock"),
    path('addlivestock/', AddLiveStockView.as_view(), name="addLiveStock"),
    path('updatecropTrans/<int:pk>/', UpdateCropTranslationView.as_view(), name="updateCropsTrans"),
    path('updatelivestockTrans/<int:pk>/', UpdateLiveStockTranslationView.as_view(), name="updateLivestockTrans"),
    path('deletecrop/<int:id>/', delete_crop, name="delete_crop"),
    path('deletelivestock/<int:id>/', delete_livestock, name="delete_livestock"),

]