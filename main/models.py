from django.contrib.auth.models import User
from django.db import models
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    rating = models.FloatField(default = 0)
    date = models.DateField(auto_now_add=True)
