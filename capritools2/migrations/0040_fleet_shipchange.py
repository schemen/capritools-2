# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0039_fleet_memberevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet_ShipChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capritools2.Character')),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capritools2.Fleet')),
                ('from_ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_ship', to='capritools2.Item')),
                ('to_ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_ship', to='capritools2.Item')),
            ],
        ),
    ]
