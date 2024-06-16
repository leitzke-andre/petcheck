from django.db import models


# Create your models here.
class Race(models.IntegerChoices):
    CAT = 1, 'Cat'
    DOG = 2, 'Dog'
    BIRD = 3, 'Bird'


class Sex(models.IntegerChoices):
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'
    OTHER = 3, 'Other'


class Pet(models.Model):
    name = models.CharField(max_length=50)
    race = models.IntegerField(choices=Race.choices, default=Race.CAT)
    breed = models.CharField(max_length=50)
    birth_date = models.DateField()
    sex = models.IntegerField(choices=Sex.choices, default=Sex.MALE)
    is_castrated = models.BooleanField()


class PetWeight(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    weight = models.IntegerField()
    date = models.DateField()
