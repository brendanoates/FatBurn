from django.contrib import admin
from .models import Person, Exercise

__author__ = 'boates'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_weight')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass
