from django.db import models
import uuid

class ItemCategory (models.TextChoices):
    MAGICAL = "Magical"
    WEAPON = "Weapon"
    ARMOUR = "Armour"
    CONSUMABLE = "Consumable"
    UNIDENTIFIED = "Unidentified"


class Equipment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    durability = models.IntegerField(default=100)
    add_attack = models.IntegerField(default=0)
    add_defense = models.IntegerField(default=0)
    add_mana = models.IntegerField(default=0)
    add_life = models.IntegerField(default=0)
    category = models.CharField(
        max_length=30,
        choices=ItemCategory.choices,
        default=ItemCategory.UNIDENTIFIED
    )
