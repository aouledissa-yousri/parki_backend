# Generated by Django 4.0.4 on 2022-05-10 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_car_municipalityzone_alter_car_parkinglot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='workAddress',
        ),
    ]
