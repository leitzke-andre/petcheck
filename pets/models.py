from django.db import models
from vet.models import Medication, Consultation


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
    weight = models.IntegerField(help_text='Weight of the animal in grams (e.g.: 2500 for 2,5kg)')
    date_and_time = models.DateTimeField()

    def __str__(self):
        return f'{self.pet} - {self.weight}g at {self.date_and_time}'


class PetMedication(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    consultation = models.ForeignKey(Consultation, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    dosage_unit = models.CharField(max_length=50, help_text='Unit of dosage (e.g.: mL, mg, tablets)')
    quantity = models.IntegerField(help_text='Quantity to be taken at a time')
    daily_doses = models.IntegerField(help_text='Number of doses to be taken over a day')

    def __str__(self):
        return f'{self.pet} - {self.medication} (from {self.start_date} to {self.end_date})'