# Generated by Django 4.2.6 on 2023-11-05 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0003_alter_advertisement_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]