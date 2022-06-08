from django.db import models
from home.models import Crops, Livestock

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=255)
    english = models.CharField(max_length=255)
    arabic = models.CharField(max_length=255, blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    cropid = models.ForeignKey(Crops, models.DO_NOTHING, db_column='cropId', blank=True, null=True)  # Field name made lowercase.
    livestockid = models.ForeignKey(Livestock, models.DO_NOTHING, db_column='livestockId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'videos'