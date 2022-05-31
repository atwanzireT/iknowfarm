from django.db import models

# Create your models here.
class User(models.Model):
    GENDER_CHOICES = [
        ('M', "Male"),
        ('F', "Female")
    ]
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    nationality = models.CharField(max_length=45)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    physical_address = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.fullname