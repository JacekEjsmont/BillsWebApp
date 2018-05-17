# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-17 09:37
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Bill', '0003_auto_20180516_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='bill',
            name='Date',
            field=models.DateTimeField(auto_now=True, verbose_name=datetime.datetime(2018, 5, 17, 9, 37, 53, 772663)),
        ),
        migrations.AlterField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Bill.Custom'),
        ),
    ]