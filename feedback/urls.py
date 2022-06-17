from .views import *
from .models import *
from django.urls import path


urlpatterns = [
    path('feedback/', feedback, name="feedback"),
    path('', feedback, name="feed"),
    path('reply_feedback/<int:pk>/', ReplyView.as_view(), name="reply_feedback"),
]