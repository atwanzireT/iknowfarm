import re
from unicodedata import name
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import uuid
from datetime import date

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=45)
    
    def __str__(self) -> str:
        return self.country

class District(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    district = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.district

class Village(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    village = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.village

class FarmerGroup(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=50, unique=True)
    registration_date = models.DateField(auto_now_add=True)
    expiry = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='A')
    recommender = models.CharField(max_length=45, blank=True, null=True)
    Village = models.ForeignKey(Village, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class SingleFarmer(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    GENDER_CHOICES = [
        ('M', "Male"),
        ('F', "Female")
    ]
    name = models.CharField(max_length=50)
    farmer_code = models.UUIDField(default=uuid.uuid4, editable=False)
    Date_of_Birth = models.DateField("Date of Birth", null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    expiry = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='A')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    recommender = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    Village = models.ForeignKey(Village, on_delete=models.CASCADE, blank=True, null=True)
    FarmerGroup = models.ForeignKey(FarmerGroup, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.name

    @property
    def age(self):
        today = date.today()
        days = today - (self.Date_of_Birth)
        year = days.days // 365
        return f"{year} years"
        