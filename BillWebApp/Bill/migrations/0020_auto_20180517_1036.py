# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-17 10:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0019_auto_20180517_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Date',
            field=models.DateTimeField(auto_now=True, verbose_name=datetime.datetime(2018, 5, 17, 10, 36, 47, 653516)),
        ),
    ]
