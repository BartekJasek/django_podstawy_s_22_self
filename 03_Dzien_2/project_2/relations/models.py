from django.db import models


# One-to-one
class Country(models.Model):
    name = models.CharField(max_length=64)


class Captial(models.Model):
    name = models.CharField(max_length=64)
    country = models.OneToOneField('Country', on_delete=models.CASCADE)


# One-to-many (ForeignKey)
class State(models.Model):
    name = models.CharField(max_length=64)


class City(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey('State', c=models.CASCADE)
