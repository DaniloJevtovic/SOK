# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('d3_primeri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_links', to='d3_primeri.Element')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_links', to='d3_primeri.Element')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribs', to='d3_primeri.Element'),
        ),
    ]
