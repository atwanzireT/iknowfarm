from unicodedata import name
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import uuid

# Create your models here.
class FarmerGroup(MPTTModel):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    registration_date = models.DateField(auto_now_add=True)
    expiry = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='A')

    class MPTTMeta:
        order_insertion_by = ['name']

class SingleFarmer(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    name = models.CharField(max_length=50)
    farmer_code = models.UUIDField(default=uuid.uuid4, editable=False)
    registration_date = models.DateField(auto_now_add=True)
    expiry = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='A')

    def __str__(self):
        return self.name