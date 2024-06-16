from django.db import models
from pets.models import Pet
from base.models import Medication


# Create your models here.
class Consultation(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField()
    veterinarian = models.CharField(max_length=50)


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
