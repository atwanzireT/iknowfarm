from django.db import models
from home.models import Crop, Livestock

# Create your models here.
class CsvFile(models.Model):
    Status_choice = [
        ('Pending', 'Pending'),
        ('Processed', 'Processed'),
    ]
    file = models.FileField(upload_to='csv/')
    status = models.CharField(max_length=10, default='pending', choices=Status_choice)
    def __str__(self):
        return self.file.name

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