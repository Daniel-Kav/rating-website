# Generated by Django 5.1.1 on 2024-09-10 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visit',
            new_name='PageVisit',
        ),
    ]
