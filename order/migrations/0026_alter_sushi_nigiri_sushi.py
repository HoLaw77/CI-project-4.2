# Generated by Django 3.2 on 2023-09-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_auto_20230909_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sushi',
            name='NIGIRI_SUSHI',
            field=models.IntegerField(choices=[(1, 'raw salmon x 3 '), (2, 'raw tuna  x 3 '), (3, 'shrimp  x 3 '), (4, 'sea urchin  x 3 '), (5, 'ikura  x 3 '), (6, 'amberjack  x 3 '), (7, 'None')], default=6),
        ),
    ]