# Generated by Django 3.2 on 2023-08-01 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20230801_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sushi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=10.0, max_digits=5)),
                ('NIGIRI_SUSHI', models.IntegerField(choices=[(1, 'raw Salmon'), (2, 'raw Tuna'), (3, 'shrimp'), (4, 'sea urchin (Uni)'), (5, 'Ikura'), (6, 'Amberjack')], default=6)),
                ('INARI_SUSHI', models.IntegerField(choices=[(1, 'Inari Sushi')], default=1)),
                ('MAKI_SUSHI', models.IntegerField(choices=[(1, '6 with 3 kinds of fish salmon, tuna, amberjack'), (2, '6 with cucumber, carrot and egg'), (3, '6 with sesame topping, cucumber, egg and crab stick inside')], default=3)),
                ('TEMAKI_SUSHI', models.IntegerField(choices=[(1, ' with Crab Stick, carrot and cucumber'), (2, 'With shrimp and cucumber'), (3, 'With Ikura, egg, and salad vegetables'), (4, 'With salmon')], default=4)),
                ('SOY_OIL', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')], default=1)),
                ('WASABI', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')], default=1)),
            ],
        ),
    ]