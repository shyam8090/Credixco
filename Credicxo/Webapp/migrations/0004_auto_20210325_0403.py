# Generated by Django 3.1.7 on 2021-03-24 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0003_remove_signup_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='first_name',
            new_name='fnmae',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='last_name',
            new_name='lname',
        ),
    ]