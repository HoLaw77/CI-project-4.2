# Generated by Django 3.2 on 2023-08-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_auto_20230805_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='BEER',
            field=models.IntegerField(choices=[(1, '1 bottle'), (2, '1 can'), (3, 'None')], default=1),
        ),
    ]
