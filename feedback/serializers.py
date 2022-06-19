from dataclasses import field
from .models import *
from rest_framework import serializers
from rest_framework import permissions


class CreateFeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("rating", "ratingtitle", "comment", "audiofile", "createdby")

class ReplyFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("repliedBy", "reply",)

