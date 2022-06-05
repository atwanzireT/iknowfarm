from django import views

from farmer.views import FarmersListView
from .models import *
from django.urls import path


urlpatterns = [
    path("", FarmersListView.as_view(), name = "farmers"),
]