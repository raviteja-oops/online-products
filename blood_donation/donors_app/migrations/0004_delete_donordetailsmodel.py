# Generated by Django 2.2.5 on 2019-11-04 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donors_app', '0003_donordetailsmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DonorDetailsModel',
        ),
    ]