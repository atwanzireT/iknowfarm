from django.db import models
from home.models import Crops

# Create your models here.
class Manual(models.Model):
    description = models.TextField(blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    audio = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manual'


class CropManuals(models.Model):
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    cropid = models.OneToOneField(Crops, on_delete=models.CASCADE, db_column='cropId', primary_key=True)  # Field name made lowercase.
    manualid = models.ForeignKey(Manual , on_delete=models.CASCADE, db_column='manualId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crop_manuals'

class Translations(models.Model):
    type = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    english = models.TextField(blank=True, null=True)
    arabic = models.TextField(blank=True, null=True)
    lugbara = models.TextField(blank=True, null=True)
    cropid = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    def __str__(self):
        return f"{self.id} {self.english[:50]}"
    class Meta:
        managed = False
        db_table = 'translations'