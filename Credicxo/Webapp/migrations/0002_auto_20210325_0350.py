# Generated by Django 3.1.7 on 2021-03-24 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='mobile',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='cpwd',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='pwd',
        ),
    ]
