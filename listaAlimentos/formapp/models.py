from django.db import models

# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.DecimalField(decimal_places=2, max_digits=7)
    fat = models.DecimalField(decimal_places=2, max_digits=7)
    carbohydrates = models.DecimalField(decimal_places=2, max_digits=7)
    date = models.DateField()
