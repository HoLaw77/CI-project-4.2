# Generated by Django 3.2 on 2023-09-12 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0027_alter_ramen_toppings_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ramen',
            name='price',
        ),
    ]