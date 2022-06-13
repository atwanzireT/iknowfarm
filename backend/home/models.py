from distutils.command.upload import upload
from django.db import models
# Create your models here.
class Crop(models.Model):
    english = models.CharField(max_length=255, blank=True, null=True)
    arabic = models.CharField(max_length=255, blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.english}"

class Livestock(models.Model):
    english = models.CharField(max_length=255, blank=True, null=True)
    arabic = models.CharField(max_length=255, blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.english}"

class UnregistredUser(models.Model):
    deviceid = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 
