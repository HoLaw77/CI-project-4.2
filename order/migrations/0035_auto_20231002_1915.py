# Generated by Django 3.2 on 2023-10-02 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0034_alter_drink_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='drink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.drink'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ramen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.ramen'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sushi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.sushi'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True),
        ),
    ]
