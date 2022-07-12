from distutils.command.upload import upload
from django.db import models
from farmer.models import *
# Create your models here.
class Crop(models.Model):
    english = models.CharField(max_length=255, blank=True, null=True)
    arabic = models.CharField(max_length=255, blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField()
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.english}"

class Livestock(models.Model):
    english = models.CharField(max_length=255, blank=True, null=True)
    arabic = models.CharField(max_length=255, blank=True, null=True)
    lugbara = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField()
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.english}"

class UnregistredUser(models.Model):
    deviceid = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

class MarketPrice(models.Model):
    commodity = models.CharField(max_length=255, blank=True, null=True)
    variety = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    retailprice = models.CharField(max_length=255, blank=True, null=True)
    wholesaleprice = models.CharField(max_length=255, blank=True, null=True)
    market = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'market_prices'


class MarketVisit(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    deviceid = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'market_visits'


class ProductSale(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    variety = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    unitprice = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    farmerid = models.ForeignKey(Farmer,  on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'product_sale'
