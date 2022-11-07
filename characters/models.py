from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=20)
    level = models.PositiveIntegerField()
    silver = models.PositiveIntegerField()
    gold = models.PositiveIntegerField()
    char_class = models.ForeignKey(
        "classes.Class",
        on_delete=models.CASCADE,
        related_name="char_class"
    )

    equipments = models.ManyToManyField(
        "equipments.Equipment",
        on_delete=models.CASCADE,
        related_name="equipments"
    )

    skills = models.ManyToManyField(
        "skills.Skill",
        on_delete=models.CASCADE,
        related_name="skills"
    )

    stats = models.OneToOneField(
        "stats.Stat",
        on_delete=models.CASCADE,
        related_name="stats"
    )