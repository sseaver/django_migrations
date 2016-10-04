# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('number', models.IntegerField()),
                ('position', models.CharField(max_length=20)),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('saves', models.IntegerField()),
                ('team', models.CharField(max_length=25)),
            ],
        ),
    ]