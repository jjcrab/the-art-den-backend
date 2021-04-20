# Generated by Django 3.2 on 2021-04-20 05:53

import art.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_auto_20210420_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='graduation_year',
            field=models.PositiveSmallIntegerField(default=art.models.current_year, validators=[django.core.validators.MinValueValidator(2019), django.core.validators.MaxValueValidator(2030)]),
        ),
    ]
