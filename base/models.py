from django.db import models


# Create your models here.
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


class Food(models.Model):
    name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    adequate_for = models.ForeignKey(Race, on_delete=models.CASCADE)
    is_for_special_needs = models.BooleanField(default=False)
    ingredients = models.TextField(blank=True)


class Disease(models.Model):
    name = models.CharField(max_length=50)
    affected_animal = models.ManyToManyField(Race)


class Medication(models.Model):
    name = models.CharField(max_length=50)
    affected_animal = models.ManyToManyField(Race)

    def __str__(self):
        return self.name
