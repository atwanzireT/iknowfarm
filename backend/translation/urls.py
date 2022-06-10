from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('crop_manual',  views.crop_manual, name="crop_manual"),
    path('manual/<int:pk>/', EngManualDetailView.as_view(), name="manual_detail"),
    path('arabic_manual/<int:pk>/', ArabicManualDetailView.as_view(), name="arabic_detail"),
    path('lugbara_manual/<int:pk>/', LugbaraManualDetailView.as_view(), name="lugbara_detail"),
    path('manual_update/<int:pk>/', UpdateManualView.as_view(), name="manual_update"),
    path('manual_arabic/<int:pk>/', UpdateArabicManualView.as_view(), name="manual_arabic"),
    path('manual_lugbara/<int:pk>/', UpdateLugbaraManualView.as_view(), name="manual_lugbara"),

]