# Generated by Django 4.2.5 on 2024-01-04 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FoundItem',
        ),
        migrations.DeleteModel(
            name='LostItem',
        ),
        migrations.DeleteModel(
            name='ReturnedItem',
        ),
    ]
