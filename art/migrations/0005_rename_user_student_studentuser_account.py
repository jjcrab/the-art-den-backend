# Generated by Django 3.2 on 2021-04-23 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_alter_student_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user',
            new_name='studentuser_account',
        ),
    ]
