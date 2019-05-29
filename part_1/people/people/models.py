from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    national_animal = models.CharField(max_length=255)


class Province(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="provinces"
    )
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()


class City(models.Model):
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, related_name="cities"
    )
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()


class Residence(models.Model):
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="residences"
    )
    address = models.CharField(max_length=255)
    year_built = models.IntegerField()


class Person(models.Model):
    residence = models.ForeignKey(
        Residence, on_delete=models.CASCADE, related_name="people"
    )
    name = models.CharField(max_length=255)
    age = models.IntegerField()
