# Generated by Django 4.0.3 on 2022-03-24 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('delivery_address', models.CharField(max_length=300)),
                ('delivery_time', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(1, 'Nowe'), (2, 'Zdefiniowano Transport'), (3, 'Zrealizowane'), (4, 'Anulowane')], default=1)),
                ('opis', models.TextField(blank=True, null=True)),
                ('lat', models.CharField(max_length=300, null=True)),
                ('lon', models.CharField(max_length=300, null=True)),
                ('distance', models.CharField(max_length=300, null=True)),
                ('time', models.CharField(max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.cars')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.drivers')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransportApp.orders')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
