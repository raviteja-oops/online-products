# Generated by Django 2.2.5 on 2019-11-03 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage_app', '0004_donordetailsmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DonorDetailsModel',
        ),
    ]