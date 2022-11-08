from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('durability', models.IntegerField(default=100)),
                ('add_attack', models.IntegerField(default=0)),
                ('add_defense', models.IntegerField(default=0)),
                ('add_mana', models.IntegerField(default=0)),
                ('add_life', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('Magical', 'Magical'), ('Weapon', 'Weapon'), ('Armour', 'Armour'), ('Consumable', 'Consumable'), ('Unidentified', 'Unidentified')], default='Unidentified', max_length=30)),
            ],
        ),
    ]
