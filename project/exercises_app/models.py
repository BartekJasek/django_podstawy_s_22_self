from django.db import models


# Create your models here.
class Band(models.Model):

    CHOICES = [
        (-1, 'not defined'),
        (0, 'rock'),
        (1, 'metal'),
        (2, 'pop'),
        (3, 'hip-hop'),
        (4, 'electronic'),
        (5, 'reggae'),
        (6, 'other')
    ]

    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=CHOICES, default=-1)


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class Article(models.Model):

    CHOICES = [
        (0, 'in progress'),
        (1, 'waiting'),
        (2, 'published')
    ]

    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    status = models.IntegerField(choices=CHOICES, default=0)
    start_publish_date = models.DateTimeField(null=True)
    end_publish_date = models.DateTimeField(null=True)


class Album(models.Model):

    CHOICES = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    title = models.CharField(max_length=128)
    year = models.IntegerField()
    rating = models.IntegerField(choices=CHOICES)
    # relacje - zad 1
    band = models.ForeignKey('Band', on_delete=models.CASCADE)
