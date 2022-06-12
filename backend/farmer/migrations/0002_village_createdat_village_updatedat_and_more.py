# Generated by Django 4.0.3 on 2022-06-11 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='village',
            name='createdat',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='village',
            name='updatedat',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='createdat',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='updatedat',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]