# Generated by Django 4.0.3 on 2022-07-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TransportApp', '0006_alter_car_user_alter_driver_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
