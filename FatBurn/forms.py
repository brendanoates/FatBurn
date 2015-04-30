from FatBurn.validators import validate_height, validate_weight

__author__ = 'boates'

from django import forms

class UserDetailsForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    first_name = forms.CharField(label='First name', max_length=100, required=True )
    last_name = forms.CharField(label='Last name', max_length=100, required=True)
    start_weight = forms.DecimalField(max_digits= 5, decimal_places=2, required=True,
                                      help_text="<br>Please enter your weight in kilograms e.g. 80.1", validators=[validate_weight])
    height = forms.DecimalField(max_digits= 4, decimal_places=3, required=True,
                                help_text="<br>Please enter your height in meters e.g. 1.60", validators=[validate_height])



