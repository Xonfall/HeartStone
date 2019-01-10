from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models


class User(AbstractUser):
    money = models.IntegerField(default=500)
