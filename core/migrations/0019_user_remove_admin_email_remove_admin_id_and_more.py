# Generated by Django 4.0.4 on 2022-05-01 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('lastname', models.CharField(default='', max_length=255)),
                ('username', models.CharField(default='', max_length=255, unique=True)),
                ('email', models.CharField(default='', max_length=255, unique=True)),
                ('phoneNumber', models.CharField(default='', max_length=255, unique=True)),
                ('password', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='email',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='id',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='name',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='password',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='username',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='email',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='id',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='name',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='password',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='username',
        ),
        migrations.RemoveField(
            model_name='municipalagent',
            name='email',
        ),
        migrations.RemoveField(
            model_name='municipalagent',
            name='id',
        ),
        migrations.RemoveField(
            model_name='municipalagent',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='municipalagent',
            name='name',
        ),
        migrations.RemoveField(
            model_name='municipalagent',
            name='password',
        ),
        migrations.RemoveField(
            model_name='municipalagent',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='municipalagent',
            name='username',
        ),
        migrations.RemoveField(
            model_name='privateagent',
            name='email',
        ),
        migrations.RemoveField(
            model_name='privateagent',
            name='id',
        ),
        migrations.RemoveField(
            model_name='privateagent',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='privateagent',
            name='name',
        ),
        migrations.RemoveField(
            model_name='privateagent',
            name='password',
        ),
        migrations.RemoveField(
            model_name='privateagent',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='privateagent',
            name='username',
        ),
        migrations.AddField(
            model_name='admin',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='municipalagent',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
        migrations.AddField(
            model_name='privateagent',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.user'),
            preserve_default=False,
        ),
    ]
