# Generated by Django 4.0.4 on 2022-04-30 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_paymentlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentlog',
            name='driver',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.driver'),
        ),
    ]
