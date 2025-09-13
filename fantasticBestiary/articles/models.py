from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    history = models.TextField()
    image = models.ImageField(upload_to='articles/images/', null=True, blank=True)

    def __str__(self):
        return self.name