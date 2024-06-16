from django.db import models
from base.models import Race, Food


class FeedingNeed(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    min_weight = models.IntegerField()
    max_weight = models.IntegerField()
    min_daily_kcal = models.IntegerField()
    max_daily_kcal = models.IntegerField()


class FoodSpecificQuantities(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    min_weight = models.IntegerField()
    max_weight = models.IntegerField()
    min_daily_quantity = models.IntegerField()
    max_daily_quantity = models.IntegerField()