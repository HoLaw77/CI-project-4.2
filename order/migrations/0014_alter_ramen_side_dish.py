# Generated by Django 3.2 on 2023-08-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_remove_ramen_noodle_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ramen',
            name='side_dish',
            field=models.IntegerField(choices=[(1, 'Gyoza dumpling'), (2, 'Edamame beans'), (3, 'Yakitori skewers (chicken, beef)'), (4, 'Tempura (Chilli squid )'), (5, 'kimchi'), (6, 'fried chicken')], default=1),
        ),
    ]
