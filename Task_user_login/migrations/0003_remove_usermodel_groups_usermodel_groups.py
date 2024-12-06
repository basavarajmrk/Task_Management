# Generated by Django 4.2.16 on 2024-12-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Task_user_login', '0002_usermodel_reports_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='groups',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='groups',
            field=models.ManyToManyField(to='auth.group'),
        ),
    ]
