# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0021_auto_20170607_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleetmember',
            name='corporation',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='capritools2.Corporation'),
        ),
    ]
