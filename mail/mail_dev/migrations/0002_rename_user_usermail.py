# Generated by Django 4.1.3 on 2022-11-17 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_dev', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserMail',
        ),
    ]