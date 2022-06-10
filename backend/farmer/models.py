from pyexpat import model
from unicodedata import name
from django.db import models
from datetime import date

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    districtid = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Recomender(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    villages = models.ForeignKey(Village, on_delete= models.CASCADE ,blank=True, null=True)
    phonenumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 
    
    def __str__(self) -> str:
        return self.name

class FarmerGroup(models.Model):
    name = models.CharField(max_length=255)
    villages = models.ForeignKey(Village, on_delete= models.CASCADE, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.name


class Farmer(models.Model):
    STATUS_CODE = [
        ('married', 'married')
    ]
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=255, blank=True, null=True)
    villages = models.ForeignKey(Village, on_delete=models.CASCADE ,blank=True, null=True)
    phonenumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=255)
    codesent = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CODE)
    expiry = models.DateTimeField()
    recommender = models.ForeignKey(Recomender, on_delete=models.CASCADE)
    group = models.ForeignKey(FarmerGroup, on_delete=models.CASCADE, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def age(self):
        from  datetime import date
        age_years = (date.today() - self.date_of_birth)
        return  int((age_years).days/365.25)

    def __str__(self) -> str:
        return self.name
