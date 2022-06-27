from datetime import date
from operator import mod
from pyexpat import model
from statistics import mode
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models

# Create your models here.

class topic(models.Model):
    top_name=models.CharField(max_length=250, unique=True)


    def __str__(self):
        return self.top_name



class Webpage(models.Model):
    topic=models.ForeignKey('topic', on_delete=models.CASCADE,)
    name=models.CharField(max_length=264, unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name


class Accessrecord(models.Model):
    name=models.ForeignKey('Webpage', on_delete=models.CASCADE,)
    date=models.DateField()

    def __str__(self):
        return str(self.date)