# Generated by Django 4.2.2 on 2024-09-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_setlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setlist',
            name='pieces',
        ),
        migrations.AddField(
            model_name='setlist',
            name='sheets',
            field=models.ManyToManyField(to='organizer.sheet'),
        ),
    ]
