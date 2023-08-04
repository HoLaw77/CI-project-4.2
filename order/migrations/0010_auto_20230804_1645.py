# Generated by Django 3.2 on 2023-08-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_ramen_soup_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ramen',
            name='ingredient_choice',
        ),
        migrations.AddField(
            model_name='ramen',
            name='toppings_choice',
            field=models.IntegerField(choices=[(1, 'Egg'), (2, 'Sea weed'), (3, 'Pork'), (4, 'Garlic')], default=3),
        ),
    ]
