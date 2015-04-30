from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from FatBurn.validators import validate_weight, validate_height

__author__ = 'Brendan'

class Person(models.Model):

    user = models.OneToOneField(User, primary_key=True)
    start_weight = models.DecimalField(max_digits= 5, decimal_places=2, default=0.00, null=True)
    height = models.DecimalField(max_digits= 4, decimal_places=3, default=0.000, null=True)

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_bmi(self):
        return self.start_weight/(self.height*self.height)



