# Generated by Django 4.1.3 on 2022-11-07 19:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('life', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('attack', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('defense', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('mana', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
