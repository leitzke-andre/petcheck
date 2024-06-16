from django.contrib import admin

from .models import Pet, PetWeight, Race
# Register your models here.
admin.site.register(Pet)
admin.site.register(PetWeight)
admin.site.register(Race)