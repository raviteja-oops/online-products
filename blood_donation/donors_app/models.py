from django.db import models
from datetime import date


class DonorDetailsModel(models.Model):
    d_name = models.CharField(max_length=30)
    d_userid = models.CharField(max_length=30,unique=True)
    d_password = models.CharField(max_length=30)
    d_gender = models.CharField(max_length=10)
    d_age = models.IntegerField()
    d_email = models.EmailField()
    d_contact = models.IntegerField()
    d_blood_group = models.CharField(max_length=10)
    d_state = models.CharField(max_length=30)
    d_city = models.CharField(max_length=30)
    d_weight = models.IntegerField()
    d_last_donation_date = models.DateField(("Date"), default=date.today)
