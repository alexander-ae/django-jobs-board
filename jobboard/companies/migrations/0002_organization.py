# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('url', models.URLField(blank=True, verbose_name='URL')),
                ('location', models.CharField(blank=True, max_length=120)),
                ('coordinates', models.CharField(blank=True, help_text='lat,lon', max_length=64)),
                ('summary', models.CharField(blank=True, max_length=128)),
                ('size', models.CharField(blank=True, choices=[('Startup', 'Startup'), ('Digital agency', 'Digital agency'), ('Small bussiness', 'Small business'), ('Medium bussiness', 'Medium business'), ('Big bussiness', 'Big business'), ('Non-profit', 'Non-profit')], max_length=64, verbose_name='Company size')),
                ('employees', models.CharField(blank=True, choices=[('1 - 5', '1 - 5'), ('5 - 10', '5 - 10'), ('10 - 100', '10 - 100'), ('100+', '100+')], max_length=64, verbose_name='Quantity of employees')),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'ordering': ['name'],
            },
        ),
    ]
