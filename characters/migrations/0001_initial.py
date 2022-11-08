# Generated by Django 4.1.3 on 2022-11-08 18:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('skills', '0001_initial'),
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('level', models.PositiveIntegerField()),
                ('silver', models.PositiveIntegerField()),
                ('gold', models.PositiveIntegerField()),
                ('char_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char_class', to='classes.class')),
                ('equipments', models.ManyToManyField(related_name='equipments', to='equipments.equipment')),
                ('skills', models.ManyToManyField(related_name='skills', to='skills.skill')),
            ],
        ),
    ]
