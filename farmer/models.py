from django.db import models
from datetime import date
import uuid

# Create your models here.

class FarmerFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='farmer/files/')
    createdat = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True, blank=True, null=True) 

    def __str__(self):
        return self.title
class District(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True, blank=True, null=True) 

    def __str__(self) -> str:
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    districtid = models.ForeignKey(District, on_delete=models.CASCADE)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.name

class Recomender(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    village = models.ForeignKey(Village, on_delete= models.CASCADE ,blank=True, null=True)
    phonenumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 
    
    def __str__(self) -> str:
        return self.name

class FarmerGroup(models.Model):
    STATUS_CODE = [
        (1, 'activate'),
        (0, 'deactivate'),
    ]

    name = models.CharField(max_length=255)
    pin = models.CharField(max_length=10)
    group_type = models.CharField(max_length=20)
    female_farmers = models.IntegerField(default=0)
    male_farmers = models.IntegerField(default=0)
    village = models.ForeignKey(Village, on_delete= models.CASCADE, blank=True, null=True)
    phonenumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    recommender = models.ForeignKey(Recomender, on_delete=models.CASCADE, blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True, default=1)
    status = models.CharField(max_length=20, choices=STATUS_CODE, blank=True, null=True)
    expiry = models.DateTimeField( blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    def __str__(self) -> str:
        return self.name


class Farmer(models.Model):
    STATUS_CODE = [
        (1, 'activate'),
        (0, 'deactivate'),
    ]

    GENDER_CODE = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255,choices=GENDER_CODE, blank=True, null=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE ,blank=True, null=True)
    phonenumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=255)
    codesent = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CODE, blank=True, null=True)
    expiry = models.DateTimeField( blank=True, null=True)
    recommender = models.ForeignKey(Recomender, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(FarmerGroup, on_delete=models.CASCADE, blank=True, null=True)
    farmer_type = models.CharField(max_length=255, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(auto_now=True) 

    # def age(self):
        # from  datetime import date
        # if self.date_of_birth:
        #     age_years = (date.today() - self.date_of_birth)
        #     return  int((age_years).days/365.25)
        # return f"NO DOB"

    def __str__(self) -> str:
        return self.name


class ExGroup(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

class ExGroupWorker(models.Model):
    group = models.ForeignKey(ExGroup, on_delete=models.CASCADE)
    district = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    designation = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=100)
    operation_area = models.CharField(max_length=100)
    module = models.CharField(max_length=9)

    def __str__(self) -> str:
        return self.name

class Sent_Code_farmer(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.farmer

class Sent_Code_farmerGroup(models.Model):
    farmer = models.ForeignKey(FarmerGroup, on_delete=models.CASCADE)
    code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.farmer