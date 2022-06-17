from django.db import models
from home.models import Crop, Livestock
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Manual(models.Model):
    TYPE_CHOICES = (
        ('crop', 'Crop'),
        ('livestock', 'Livestock'),
    )
    type = models.CharField( choices=TYPE_CHOICES, max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    english = RichTextField(blank=True, null=True)
    arabic = RichTextField(blank=True, null=True)
    lugbara = RichTextField(blank=True, null=True)
    english_audio = models.FileField(upload_to='audio/english/', blank=True, null=True)
    arabic_audio = models.FileField(upload_to='audio/arabic/', blank=True, null=True)
    lugbara_audio = models.FileField(upload_to='audio/lugbara/', blank=True, null=True)
    cropid = models.ForeignKey(Crop, on_delete=models.CASCADE, blank=True, null=True)
    livestockid = models.ForeignKey(Livestock, on_delete=models.CASCADE, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.id} {self.title[:50]}"