from django.db import models
from django.core import validators


class Class(models.Model):
    name = models.CharField(max_length=30)
    life = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
    attack = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
    defense = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
    mana = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
