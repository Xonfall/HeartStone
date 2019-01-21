from django.core.validators import MinValueValidator
from django.db import models

from user.models import User
from cards.models import Card


# Create your models here.

class Buy(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField(validators=[MinValueValidator(1)], default=0)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Exchange(models.Model):
    id = models.AutoField(primary_key=True)
    exchange_statut = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_sender = models.ForeignKey(Card, related_name='card_sender', on_delete=models.CASCADE)
    card_receiver = models.ForeignKey(Card, null=True, related_name='card_receiver', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
