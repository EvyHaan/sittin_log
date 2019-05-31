from django.contrib import admin
from .models import Family, Pet, Household

# Register your models here.
admin.site.register((Family, Pet, Household))