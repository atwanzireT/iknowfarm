from django.db import models
from home.models import Crop, Livestock

# Create your models here.
class VideoUpload(models.Model):
    title = models.CharField(max_length=45)
    english_video = models.FileField(upload_to='english_videos/', blank=True, null=True)
    arabic_video = models.FileField(upload_to='arabic_videos/', blank=True, null=True)
    lugba_video = models.FileField(upload_to='lugba_videos/', blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    crop_id = models.ForeignKey(Crop, on_delete=models.CASCADE, blank=True, null=True)
    Livestock_id = models.ForeignKey(Livestock, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.title