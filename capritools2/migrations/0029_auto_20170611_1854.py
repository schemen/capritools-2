# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0028_fleet_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='active',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
