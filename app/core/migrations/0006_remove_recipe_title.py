# Generated by Django 3.0.6 on 2020-05-10 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='title',
        ),
    ]