# Generated by Django 2.2 on 2019-05-16 15:38

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='MyUser',
        ),
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
