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
<<<<<<< HEAD
    # )
=======
    # )
    
>>>>>>> 344ce6b704b4f36f4296adccf227adb22fde6343
