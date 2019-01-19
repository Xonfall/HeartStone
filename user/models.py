from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.db import models



class User(AbstractUser):
    follow = models.ManyToManyField("self", through='Follow', blank=True, symmetrical=False)
    money = models.IntegerField(default=500)
    objects = UserManager()

    def __str__(self):
        return "{}".format(self.username)


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='followings', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)