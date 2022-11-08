# Generated by Django 4.1.3 on 2022-11-08 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_char', to=settings.AUTH_USER_MODEL),
        ),
    ]
