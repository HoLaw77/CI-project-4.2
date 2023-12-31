# Generated by Django 3.2 on 2023-10-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0050_auto_20231026_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='beer',
            field=models.IntegerField(choices=[(1, '1 bottle Asahi Super Dry'), (2, '1 bottle Saporro Premium'), (3, '1 bottle Echigo Koshihikari'), (4, '1 bottle Orion Premium Draft Beer'), (5, 'None')]),
        ),
        migrations.AlterField(
            model_name='drink',
            name='choya',
            field=models.IntegerField(choices=[(1, '1 bottle original favor'), (2, '1 bottle hoeny favor'), (3, '1 bottle peach favor'), (4, 'None')]),
        ),
        migrations.AlterField(
            model_name='drink',
            name='green_tea',
            field=models.IntegerField(choices=[(1, '1 cup'), (2, 'None')]),
        ),
        migrations.AlterField(
            model_name='drink',
            name='sake',
            field=models.IntegerField(choices=[(1, '1 bottle Dassai Sake'), (2, '1 bottle Kubota Sake'), (3, '1 bottle Yamamoto Sake'), (4, '1 bottle Juyondai Sake'), (5, 'None')]),
        ),
        migrations.AlterField(
            model_name='drink',
            name='water',
            field=models.IntegerField(choices=[(1, '1 cup'), (2, 'None')]),
        ),
        migrations.AlterField(
            model_name='sushi',
            name='inari_sushi',
            field=models.IntegerField(choices=[(1, 'Inari Sushi  x 3 '), (2, 'None')]),
        ),
        migrations.AlterField(
            model_name='sushi',
            name='maki_sushi',
            field=models.IntegerField(choices=[(1, 'salmon, tuna, amberjack x 6'), (2, 'cucumber, carrot and egg x 6'), (3, 'sesame, cucumber, egg, crab stick x 6'), (4, 'None')]),
        ),
        migrations.AlterField(
            model_name='sushi',
            name='nigiri_sushi',
            field=models.IntegerField(choices=[(1, 'raw salmon x 3 '), (2, 'raw tuna  x 3 '), (3, 'shrimp  x 3 '), (4, 'sea urchin  x 3 '), (5, 'ikura  x 3 '), (6, 'amberjack  x 3 '), (7, 'None')]),
        ),
        migrations.AlterField(
            model_name='sushi',
            name='soy_oil',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='sushi',
            name='temaki_sushi',
            field=models.IntegerField(choices=[(1, 'Crab, cucumber x 3 '), (2, 'shrimp, cucumber  x 3 '), (3, 'Ikura, egg, salad  x 3 '), (4, 'Salmon  x 3 '), (5, 'None')]),
        ),
        migrations.AlterField(
            model_name='sushi',
            name='wasabi',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'No')]),
        ),
    ]
