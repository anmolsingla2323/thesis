from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Examinor(models.Model):
    examinor_username = models.CharField(primary_key=True, max_length = 120)
    examinor_password = models.CharField(max_length=128)
    examinor_name = models.CharField(max_length=100)
    examinor_id = models.IntegerField()
    examinor_email = models.EmailField()
    examinor_contact= models.BigIntegerField()

class thesis(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    time = models.TimeField(default=timezone.now)
    date = models.DateTimeField(default=timezone.now)
    field = models.CharField(max_length=100)
    assigned = models.ForeignKey(Examinor, on_delete=models.CASCADE)
    filepass = models.CharField(max_length=100)
    feedack = models.FileField(upload_to = 'feedback')
    file = models.FileField(upload_to = 'THESI')