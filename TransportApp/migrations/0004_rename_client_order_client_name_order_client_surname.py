# Generated by Django 4.0.3 on 2022-06-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TransportApp', '0003_account_alter_car_user_alter_driver_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='client',
            new_name='client_name',
        ),
        migrations.AddField(
            model_name='order',
            name='client_surname',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
