import json
from django.db import models

class store(models.Model):
    storeid = models.IntegerField(primary_key=True)
    storename = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.storeid
    
class dj(models.Model):
    username = models.CharField(max_length=100)
    msgtime = models.CharField(max_length=50)
    star = models.PositiveIntegerField()
    comment = models.CharField(max_length=5000)
    effflag = models.PositiveIntegerField()
    storeid = models.ForeignKey(store, on_delete=models.CASCADE)
     
