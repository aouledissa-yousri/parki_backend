# Generated by Django 4.0.4 on 2022-05-10 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_municipalityzone_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='MunicipalityZone',
            new_name='municipalityZone',
        ),
    ]
