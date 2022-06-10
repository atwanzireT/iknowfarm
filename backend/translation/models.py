from django.db import models
from home.models import Crop, Livestock
from ckeditor.fields import RichTextField

# Create your models here.
class Translation(models.Model):
    title = models.CharField(max_length=255)
    english = RichTextField(blank=True, null=True)
    arabic = RichTextField(blank=True, null=True)
    lugbara = RichTextField(blank=True, null=True)
    cropid = models.ForeignKey(Crop, on_delete=models.CASCADE, blank=True, null=True)
    livestockid = models.ForeignKey(Livestock, on_delete=models.CASCADE, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.id} {self.english[:50]}"