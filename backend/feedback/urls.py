from .views import *
from .models import *
from django.urls import path


urlpatterns = [
    path('feedback/', feedback, name="feedback"),
    path('', feedback, name="feed"),
]