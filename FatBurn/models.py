from django.db import models

__author__ = 'Brendan'

class Person(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    # weight = models.CharField()