from django.db import models
from django.contrib.auth.models import User, Group


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=250)

    def __str__(self):
        return self.user.username


class Country(models.Model):

    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.TextField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
