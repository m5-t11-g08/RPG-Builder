# Generated by Django 4.1.3 on 2022-11-03 15:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classes", "0004_alter_class_attack_alter_class_defense_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="class",
            name="life",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        1, message="numero maior que 0"
                    )
                ]
            ),
        ),
    ]