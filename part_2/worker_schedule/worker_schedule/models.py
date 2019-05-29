from django.db import models

class Shift(models.Model):
  day = models.CharField(max_length=255)
  time_start = models.IntegerField()
  time_end = models.IntegerField()

class Worker(models.Model):
  name = models.CharField(max_length=255)
  wage = models.IntegerField()
  shifts = models.ManyToManyField(Shift, related_name="workers")