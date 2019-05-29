from django.db import models


class Film(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()


class Viewer(models.Model):
    name = models.CharField(max_length=255)
    viewing_history = models.ManyToManyField(Film)
