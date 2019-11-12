from django.db import models

class BloodRequestsModel(models.Model):
    rno = models.AutoField(primary_key=True)
    rname = models.CharField(max_length=30)
    rcontact = models.IntegerField()
    rarea = models.CharField(max_length=30)
    rblood = models.CharField(max_length=10)

