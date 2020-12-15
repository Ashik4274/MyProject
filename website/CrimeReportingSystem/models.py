from django.db import models
from django.contrib.auth.models import User


class Crimelist (models.Model):
    crimename = models.CharField(max_length=200)
    cdes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, default=None , on_delete=models.CASCADE)


    def __str__(self):
        return self.crimename


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.IntegerField()

    def __str__(self):
        return self.username

