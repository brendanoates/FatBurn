__author__ = 'boates'
from django.core.exceptions import ValidationError

def validate_weight(value):
    if not (is_number(value) and value > 0 and value < 350):
        raise ValidationError('{} is not within the valid weight range'.format(value))

def validate_height(value):
    if not (is_number(value) and value > 0.5 and value < 2.5):
        raise ValidationError('{} is not within the valid height range'.format(value))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False