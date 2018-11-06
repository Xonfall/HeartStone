from django.db import models


# Create your models here.

class Type_Card(models.Model):
    name = models.CharField(max_length=100)


class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    type_card_id = models.ForeignKey(Type_Card, on_delete=models.CASCADE)
