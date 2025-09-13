from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} el lugar"
    
class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    work_is_at_night = models.BooleanField(default=False)

    def __str__(self):
        return f"El restaurante en {self.place.name}"

class Food(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Chef(models.Model):
    name = models.CharField(max_length=200)
    experience = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    food = models.ManyToManyField(Food)

    def __str__(self):
        return f"Chef {self.name} con {self.experience} años de experiencia"