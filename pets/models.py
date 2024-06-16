from enum import Enum

from django.db import models


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50)
    race = models.IntegerField
    breed = models.CharField(max_length=50)
    birth_date = models.DateField()
    sex = models.IntegerField
    is_castrated = models.BooleanField()


class PetWeight(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    weight = models.IntegerField()
    date = models.DateField()


class Race(Enum):
    CAT = 1
    DOG = 2
    BIRD = 3


class Sex(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3
