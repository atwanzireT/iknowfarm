from dataclasses import field
from .models import *
from rest_framework import serializers

    # rating = models.CharField(max_length=255, blank=True, null=True)
    # ratingtitle = models.CharField(max_length=255, blank=True, null=True)
    # comment = models.CharField(max_length=255, blank=True, null=True)
    # audiofile = models.CharField(max_length=255, blank=True, null=True)
    # reply = models.TextField(blank=True, null = True, default="null")
    # createdby = models.ForeignKey(Farmer, on_delete=models.CASCADE, db_column='createdby')
    # createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    # updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

class CreateFeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("rating", "ratingtitle", "comment", "audiofile")

class ReplyFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        models = Feedback
        fields = ("reply",)
