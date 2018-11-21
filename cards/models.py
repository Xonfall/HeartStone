from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Type_Card(models.Model):
    name = models.CharField(max_length=100)


class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    attack = models.IntegerField(validators=[MinValueValidator(1)], default=0)
    health = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    cost = models.IntegerField(validators=[MinValueValidator(1)], default=0)
    img = models.CharField(max_length=255, null=True)
    type_card = models.ForeignKey(Type_Card, on_delete=models.CASCADE)