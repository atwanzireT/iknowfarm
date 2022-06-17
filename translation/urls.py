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

    # Livestock Urls
    path('livestock_manual',  views.livestock_manual, name="livestock_manual"),
    path('livestock_manual/<int:pk>/', EngManualDetailView.as_view(), name="livestock_manual_detail"),
    path('livestock_arabic_manual/<int:pk>/', ArabicManualDetailView.as_view(), name="livestock_arabic_detail"),
    path('livestock_lugbara_manual/<int:pk>/', LugbaraManualDetailView.as_view(), name="livestock_lugbara_detail"),
    path('livestock_manual_update/<int:pk>/', UpdateLiveManualView.as_view(), name="livestock_manual_update"),
    path('livestock_manual_arabic/<int:pk>/', UpdateArabicLiveManualView.as_view(), name="livestock_manual_arabic"),
    path('livestock_manual_lugbara/<int:pk>/', UpdateLiveLugbaraManualView.as_view(), name="livestock_manual_lugbara"),

]