# Generated by Django 2.2.1 on 2019-05-29 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='postal',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='province',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='street_address',
        ),
    ]
