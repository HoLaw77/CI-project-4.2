# Generated by Django 3.2 on 2023-08-04 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ramen',
            name='soup_choice',
            field=models.IntegerField(choices=[(1, 'pork bones soup'), (2, 'Salt soup'), (3, 'miso soup'), (4, 'soy sauce soup')], default=1),
        ),
    ]
