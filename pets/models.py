from django.db import models


class Sex(models.IntegerChoices):
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'
    OTHER = 3, 'Other'


class Race(models.Model):
    common_name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50)
    is_exotic = models.BooleanField()

    def __str__(self):
        return f'{self.common_name} ({self.scientific_name})'


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
    weight = models.IntegerField()
    date_and_time = models.DateTimeField()

    def __str__(self):
        return f'{self.pet} - {self.weight}g at {self.date_and_time}'


