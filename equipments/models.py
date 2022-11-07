from django.db import models


class ItemCategory (models.TextChoices):
    MAGICAL = "Magical"
    WEAPON = "Weapon"
    ARMOUR = "Armour"
    CONSUMABLE = "Consumable"
    UNIDENTIFIED = "Unidentified"

class Equipment(models.Model):
    name = models.CharField(max_length=30, unique=True)
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

    # characters = models.ManyToManyField(Characters, related_name= "character")



# Create your models here.
