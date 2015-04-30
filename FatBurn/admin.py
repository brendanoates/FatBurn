from django.contrib import admin
from .models import Person

__author__ = 'boates'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_weight')
    pass

