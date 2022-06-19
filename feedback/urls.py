from .views import *
from .models import *
from django.urls import path
from .serializers import *



urlpatterns = [
    path('feedback/', feedback, name="feedback"),
    # path('', feedback, name="feed"),
    path('reply_feedback/<int:pk>/', ReplyView.as_view(), name="reply_feedback"),

    # Feedback Apis
    path('feedback/api/', CreateFeedbackList .as_view(), name="feed__api"),
    path('reply_feedback/api/', ReplyFeedbackList.as_view(), name="reply_feedback_api"),
]