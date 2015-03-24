# coding: utf-8
from django.db import models

from countries_field.fields import CountriesField


class TestCountriesModel(models.Model):
    """ Test model
    """
    countries = CountriesField()


class TestCountriesParentModel(models.Model):
    countries = CountriesField()

    class Meta:
        abstract = True


class TestCountriesChildModel(TestCountriesParentModel):
    class Meta:
        abstract = False