# Generated by Django 3.2 on 2023-09-17 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0031_auto_20230917_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='CHOYA',
            field=models.IntegerField(choices=[(1, '1 bottle original favor'), (2, '1 bottle hoeny favor'), (3, '1 bottle peach favor'), (4, 'None')], default=1),
        ),
    ]
