# Generated by Django 4.0.4 on 2022-05-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_user_remove_admin_email_remove_admin_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tries',
            field=models.IntegerField(default=0),
        ),
    ]
