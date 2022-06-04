from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class UserProfile(models.Model):
#     GENDER_CHOICES = [
#         ('M', "Male"),
#         ('F', "Female")
#     ]

#     APP_USERS = [
#         ('T', 'True'),
#         ('F', 'False')
#     ]

#     REGISTERED_USERS = [
#         ('T', 'True'),
#         ('F', 'False')
#     ]
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     fullname = models.CharField(max_length=50)
#     email = models.EmailField()
#     nationality = models.CharField(max_length=45)
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
#     physical_address = models.CharField(max_length=45)
#     app_user = models.CharField(choices=APP_USERS, max_length=10)
#     registered  = models.CharField(choices=REGISTERED_USERS, max_length=10, default='F')
    

#     def __str__(self) -> str:
#         return self.user.username