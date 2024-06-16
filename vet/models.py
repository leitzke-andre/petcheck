from django.db import models
from pets.models import Pet, Race


# Create your models here.
class Consultation(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField()
    veterinarian = models.CharField(max_length=50)


class Disease(models.Model):
    name = models.CharField(max_length=50)


class Medication(models.Model):
    name = models.CharField(max_length=50)
    affected_animal = models.ManyToManyField(Race)