from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('logout', views.logout_func, name='logout'),
    path('profile', views.Profile, name='profile'),
    path('edit_profile', UserEditView.as_view(), name = "edit_profile"),
]