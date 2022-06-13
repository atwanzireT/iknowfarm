from django.db import models
from home.models import Crop, Livestock
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Manual(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    english = RichTextField(blank=True, null=True)
    arabic = RichTextField(blank=True, null=True)
    lugbara = RichTextField(blank=True, null=True)
    cropid = models.ForeignKey(Crop, on_delete=models.CASCADE, blank=True, null=True)
    livestockid = models.ForeignKey(Livestock, on_delete=models.CASCADE, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.id} {self.title[:50]}"

    def get_absolute_url(self):
        return f"/translation/crop_manual{self.id}"