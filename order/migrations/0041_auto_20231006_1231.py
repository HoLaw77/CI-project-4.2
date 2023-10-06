# Generated by Django 3.2 on 2023-10-06 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0040_auto_20231006_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='drink',
        ),
        migrations.AddField(
            model_name='order',
            name='drink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.drink'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='ramen',
        ),
        migrations.AddField(
            model_name='order',
            name='ramen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.ramen'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='sushi',
        ),
        migrations.AddField(
            model_name='order',
            name='sushi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.sushi'),
        ),
    ]
