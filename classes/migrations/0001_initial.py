import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('life', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('attack', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('defense', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('mana', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
