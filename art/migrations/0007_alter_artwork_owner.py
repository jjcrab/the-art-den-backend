# Generated by Django 3.2 on 2021-04-22 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art', '0006_alter_artwork_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_artworks', to=settings.AUTH_USER_MODEL),
        ),
    ]
