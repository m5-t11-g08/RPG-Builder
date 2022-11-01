from enum import unique
from django.db import models
from traitlets import default

class Skill(models.Model):
    name = models.CharField(max_length=30, unique=True)
    damage = models.IntegerField(null=False)
    mana_cost = models.IntegerField(default = 0)

    # characters = models.ManyToManyField(Characters, related_name= "character")

# exenplo de criaçao de skill
# python manage.py shell 
# bola_de_fogo = Skill.objects.create(name = 'bola de fogo', damage = 50, mana_cost = 10)