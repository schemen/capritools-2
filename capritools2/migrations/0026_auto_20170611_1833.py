# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0025_auto_20170610_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('motd', models.TextField()),
                ('voice_enabled', models.BooleanField()),
                ('registered', models.BooleanField()),
                ('free_move', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Fleet_Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('takes_fleet_warp', models.BooleanField()),
                ('role', models.CharField(max_length=16)),
                ('role_name', models.TextField()),
                ('join_time', models.DateTimeField()),
                ('alliance', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fleet_members', to='capritools2.Alliance')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fleet_members', to='capritools2.Character')),
                ('corporation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fleet_members', to='capritools2.Corporation')),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='capritools2.Fleet')),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fleet_members', to='capritools2.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Fleet_Squad',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='squads', to='capritools2.Fleet')),
            ],
        ),
        migrations.CreateModel(
            name='Fleet_Wing',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('fleet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wings', to='capritools2.Fleet')),
            ],
        ),
        migrations.AddField(
            model_name='fleet_squad',
            name='wing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='squads', to='capritools2.Fleet_Wing'),
        ),
        migrations.AddField(
            model_name='fleet_member',
            name='squad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='capritools2.Fleet_Squad'),
        ),
        migrations.AddField(
            model_name='fleet_member',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fleet_members', to='capritools2.System'),
        ),
        migrations.AddField(
            model_name='fleet_member',
            name='wing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='capritools2.Fleet_Wing'),
        ),
    ]
