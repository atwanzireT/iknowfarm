from django.db import models
from farmer.models import *

# Create your models here.
class Feedback(models.Model):
    rating = models.CharField(max_length=255, blank=True, null=True)
    ratingtitle = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    audiofile = models.CharField(max_length=255, blank=True, null=True)
    repliedBy = models.CharField(max_length=255, blank=True, null=True)
    reply = models.TextField(blank=True, null = True, default="null")
    createdby = models.ForeignKey(Farmer, on_delete=models.CASCADE, db_column='createdby')
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    def __str__(self) -> str:
        return self.ratingtitle
