# Generated by Django 4.1.3 on 2022-11-09 20:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('damage', models.IntegerField()),
                ('mana_cost', models.IntegerField(default=0)),
            ],
        ),
    ]
