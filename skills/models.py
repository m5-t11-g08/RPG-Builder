from django.db import models

import uuid

class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30, unique=True)
    damage = models.IntegerField(null=False)
    mana_cost = models.IntegerField(default = 0)