from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class thesis(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    time = models.TimeField(default=timezone.now)
    date = models.DateTimeField(default=timezone.now)
    field = models.CharField(max_length=100)
    assigned = models.ForeignKey(User, on_delete=models.CASCADE)
    filepass = models.CharField(max_length=100)
    feedack = models.FileField(upload_to = 'feedback')
    file = models.FileField(upload_to = 'THESI')