from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_char', to=settings.AUTH_USER_MODEL),
        ),
    ]
