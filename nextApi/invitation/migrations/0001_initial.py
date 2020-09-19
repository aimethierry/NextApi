# Generated by Django 3.1 on 2020-08-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeEmail', models.CharField(blank=True, max_length=100)),
                ('confirmed', models.FloatField()),
                ('sender_username', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
