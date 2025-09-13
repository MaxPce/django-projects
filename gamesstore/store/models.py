from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Gender(models.Model):
    type_gender = models.CharField(max_length=100)

    def __str__(self):
        return self.type_gender
    
class VideoGame(models.Model):
    name = models.CharField(max_length=100)
    on_stock = models.BooleanField(default=False)
    score = models.DecimalField(max_digits=2, decimal_places=1,validators=[MinValueValidator(0.0)])

    gender = models.ForeignKey(Gender,on_delete=models.CASCADE, related_name='video_games')

    def __str__(self):
        return self.name