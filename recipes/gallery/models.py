from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/image')

    def __str__(self):
        return self.title