# Generated by Django 4.2.3 on 2023-08-03 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='firstname',
            new_name='name',
        ),
    ]
