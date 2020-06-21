from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone


class Country(models.Model):

    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=250)
    phone_number = models.TextField(max_length=10)
    age = models.IntegerField()
    sex = models.TextField()
    profile_picture = models.TextField()
    description = models.TextField(max_length=50000)
    country_origin = models.OneToOneField(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class City(models.Model):

    name = models.TextField(max_length=100)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    author_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)


class Image(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.TextField()


class CityRating(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    night_life = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    sights = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    transportation = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    food = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    hospitality = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    crime_rate = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
