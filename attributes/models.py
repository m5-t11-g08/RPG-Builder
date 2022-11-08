from django.db import models

import uuid

class Attribute(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    life = models.PositiveIntegerField()
    attack = models.PositiveIntegerField()
    defense = models.PositiveIntegerField()
    mana = models.PositiveIntegerField()

    