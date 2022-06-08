from django.db import models

# Create your models here.
class Translations(models.Model):
    type = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    english = models.TextField(blank=True, null=True)
    arabic = models.TextField(blank=True, null=True)
    lugbara = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'translations'