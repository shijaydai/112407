import json
from django.db import models

class dj(models.Model):
    username = models.CharField(max_length=100)
    msgtime = models.CharField(max_length=50)
    star = models.PositiveIntegerField()
    comment = models.CharField(max_length=5000)
    effflag = models.PositiveIntegerField()
     
