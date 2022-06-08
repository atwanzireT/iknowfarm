from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Crops(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'crops'

class Livestock(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'livestock'

