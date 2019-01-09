from django.core.validators import MinValueValidator
from django.db import models

from user.models import User


# Create your models here.

class Rarity_card(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Race_card(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    attack = models.IntegerField(validators=[MinValueValidator(1)], default=0)
    health = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    cost = models.IntegerField(validators=[MinValueValidator(1)], default=0)
    img = models.CharField(max_length=255, null=True)
    rarity_card = models.ForeignKey(Rarity_card, on_delete=models.CASCADE)
    race_card = models.ForeignKey(Race_card, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name