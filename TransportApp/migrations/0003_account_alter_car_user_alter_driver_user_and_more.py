# Generated by Django 4.0.3 on 2022-03-24 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TransportApp', '0002_rename_drivers_driver_rename_orders_order_car_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('lat', models.CharField(max_length=255)),
                ('long', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.account'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.account'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.account'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.account'),
        ),
    ]