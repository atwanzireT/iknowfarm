from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
from farmer.models import *

# Create your models here.
class Feedback(models.Model):
    rating = models.CharField(max_length=255, blank=True, null=True)
    ratingtitle = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    audiofile = models.CharField(max_length=255, blank=True, null=True)
    createdby = models.ForeignKey(Farmers, on_delete=models.CASCADE, db_column='createdby')
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedback'