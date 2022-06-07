from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Feedback(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Relied', 'Relied'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=1)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='True')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'comment', 'rate']