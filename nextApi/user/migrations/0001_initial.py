# Generated by Django 3.1 on 2020-08-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usesrname', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('company', models.CharField(blank=True, max_length=120, null=True)),
                ('password', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
