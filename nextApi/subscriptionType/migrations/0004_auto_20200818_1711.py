# Generated by Django 3.1 on 2020-08-18 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptionType', '0003_delete_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='starDate',
        ),
    ]
