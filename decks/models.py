from django.db import models

# Create your models here.
from cards.models import Cards
from user.models import User


class Deck(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Cards)