from django.db import models
from enum import Enum
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class GenderChoice(Enum):
    Male = "Male"
    Female = "Female"


class Actor(models.Model):
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=7,choices=[(tag, tag.value) for tag in GenderChoice])
    birth_date = models.DateField()


class Movie(models.Model):
    title = models.CharField(max_length=25)
    release_date = models.DateField()
    actors = models.ManyToManyField('Actor', through='MovieCast')


class MovieCast(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    cast = models.ForeignKey('Actor', on_delete=models.CASCADE)
    role = models.CharField(max_length=25)


class MovieRating(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    no_of_ratings = models.IntegerField()

