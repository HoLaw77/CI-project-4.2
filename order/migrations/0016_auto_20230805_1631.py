# Generated by Django 3.2 on 2023-08-05 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_alter_ramen_side_dish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sushi',
            name='INARI_SUSHI',
            field=models.IntegerField(choices=[(1, 'Inari Sushi  x 3 '), (2, 'None')], default=1),
        ),
        migrations.AlterField(
            model_name='sushi',
            name='NIGIRI_SUSHI',
            field=models.IntegerField(choices=[(1, 'raw Salmon x 3 '), (2, 'raw Tuna  x 3 '), (3, 'shrimp  x 3 '), (4, 'sea urchin (Uni)  x 3 '), (5, 'Ikura  x 3 '), (6, 'Amberjack  x 3 '), (7, 'None')], default=6),
        ),
        migrations.AlterField(
            model_name='sushi',
            name='TEMAKI_SUSHI',
            field=models.IntegerField(choices=[(1, ' with Crab Stick, carrot and cucumber  x 3 '), (2, 'With shrimp and cucumber  x 3 '), (3, 'With Ikura, egg, and salad vegetables  x 3 '), (4, 'With salmon  x 3 '), (5, 'None')], default=4),
        ),
    ]