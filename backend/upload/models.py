from django.db import models
from home.models import Crop, Livestock

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    english = models.CharField(max_length=255)
    arabic = models.CharField(max_length=255, blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    cropid = models.ForeignKey(Crop, on_delete=models.CASCADE, blank=True)
    livestockid = models.ForeignKey(Livestock, on_delete=models.CASCADE, blank=True)
    livestockid = models.ForeignKey(Livestock, on_delete=models.CASCADE)  # Field name made lowercase.
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 