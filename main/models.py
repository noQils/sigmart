from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    rating = models.FloatField()
    date = models.DateField(auto_now_add=True)
