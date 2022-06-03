from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Crop(models.Model):
    name = models.CharField(max_length=45)
    arabic = models.CharField(max_length=45)
    lugbar = models.CharField(max_length=45)
    image = models.ImageField(upload_to ="crops")

    def __str__(self):
        return self.name

class Livestock(models.Model):
    name = models.CharField(max_length=45)
    arabic = models.CharField(max_length=45)
    lugbar = models.CharField(max_length=45)
    image = models.ImageField(upload_to = "livestock")

    def __str__(self):
        return self.name