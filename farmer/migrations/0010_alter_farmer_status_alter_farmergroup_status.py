# Generated by Django 4.0.3 on 2022-06-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0009_farmergroup_status_sent_code_farmergroup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'activate'), (0, 'deactivate')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='farmergroup',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'activate'), (0, 'deactivate')], max_length=20, null=True),
        ),
    ]