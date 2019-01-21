from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(validators=[MinValueValidator(1)], default=0)

    def __str__(self):
        return self.name
