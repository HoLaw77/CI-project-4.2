# Generated by Django 3.2 on 2023-10-16 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0046_alter_confirm_number_of_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirm',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='confirm', to='order.order'),
        ),
    ]
