# Generated by Django 4.1.3 on 2022-11-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_dev', '0003_alter_usermail_timesent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermail',
            name='STATUS',
            field=models.CharField(default='Не отправлено', max_length=20, verbose_name='Статус отправки'),
        ),
    ]