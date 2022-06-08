from unicodedata import name
from django.db import models
from datetime import date

# Create your models here.
class Farmers(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    phonenumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    pin = models.CharField(max_length=255)
    grouptype = models.CharField(max_length=255, blank=True, null=True)
    registrationtype = models.IntegerField(blank=True, null=True)
    femalefarmers = models.CharField(max_length=255, blank=True, null=True)
    malefarmers = models.CharField(max_length=255, blank=True, null=True)
    codesent = models.IntegerField(blank=True, null=True)
    sponsor = models.CharField(max_length=255, blank=True, null=True)
    farmertype = models.CharField(max_length=255, blank=True, null=True)
    village = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    status = models.IntegerField()
    expiry = models.DateTimeField()
    recommender = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farmers'