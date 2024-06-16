from django.db import models
from base.models import Race, Sex


class Pet(models.Model):
    name = models.CharField(max_length=50)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    breed = models.CharField(max_length=50)
    birth_date = models.DateField()
    sex = models.IntegerField(choices=Sex.choices, default=Sex.MALE)
    is_castrated = models.BooleanField()

    def __str__(self):
        return self.name


class PetWeight(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    weight = models.IntegerField(help_text='Weight of the animal in grams (e.g.: 2500 for 2,5kg)')
    date_and_time = models.DateTimeField()

    def __str__(self):
        return f'{self.pet} - {self.weight}g at {self.date_and_time}'


