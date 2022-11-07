from django.db import models
import uuid


class Character(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=20, unique=True)
    level = models.PositiveIntegerField()
    silver = models.PositiveIntegerField()
    gold = models.PositiveIntegerField()
    
    char_class = models.ForeignKey(
        "classes.Class",
        on_delete=models.CASCADE,
        related_name="char_class",
    )

    equipments = models.ManyToManyField(
        "equipments.Equipment",
        related_name="equipments"
    )

    skills = models.ManyToManyField(
        "skills.Skill",
        related_name="skills"
    )

    # stats = models.OneToOneField(
    #     "stats.Stat",
    #     on_delete=models.CASCADE,
    #     related_name="stats"
    # )
    