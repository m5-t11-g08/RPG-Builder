from django.db import models

import uuid

class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30, unique=True)
    damage = models.IntegerField(null=False)
    mana_cost = models.IntegerField(default = 0)

    # characters = models.ManyToManyField(Characters, related_name= "character")

# exenplo de criaçao de skill
# python manage.py shell 
# bola_de_fogo = Skill.objects.create(name = 'bola de fogo', damage = 50, mana_cost = 10)
# max_digits=5, decimal_places=2