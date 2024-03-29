# Generated by Django 2.2.5 on 2019-11-03 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('donors_app', '0002_delete_donordetailsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorDetailsModel',
            fields=[
                ('d_no', models.AutoField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=30)),
                ('d_userid', models.CharField(max_length=30, unique=True)),
                ('d_password', models.CharField(max_length=30)),
                ('d_gender', models.CharField(max_length=10)),
                ('d_age', models.IntegerField()),
                ('d_email', models.EmailField(max_length=254)),
                ('d_contact', models.IntegerField()),
                ('d_blood_group', models.CharField(max_length=10)),
                ('d_state', models.CharField(max_length=30)),
                ('d_city', models.CharField(max_length=30)),
                ('d_weight', models.IntegerField()),
                ('d_last_donation_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]
