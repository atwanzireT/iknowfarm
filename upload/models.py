from django.db import models
from home.models import Crop, Livestock

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    english = models.FileField(upload_to='videos/english/', blank=True, null=True)
    arabic = models.FileField(upload_to='videos/arabic/', blank=True, null=True)
    lugbara = models.FileField(upload_to='videos/lugbara/', blank=True, null=True)
    cropid = models.ForeignKey(Crop, on_delete=models.CASCADE, blank=True)
    livestockid = models.ForeignKey(Livestock, on_delete=models.CASCADE, blank=True, null=True)
    livestockid = models.ForeignKey(Livestock, on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.title