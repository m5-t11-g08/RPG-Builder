from django.db import models
from django.core import validators
import uuid


class Class(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    life = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
    attack = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
    defense = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
    mana = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
