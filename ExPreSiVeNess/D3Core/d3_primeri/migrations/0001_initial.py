# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=50)),
                ('opis', models.TextField(max_length=200)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=8)),
                ('na_akciji', models.BooleanField(verbose_name='na akciji')),
            ],
        ),
        migrations.CreateModel(
            name='Kategorija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaka', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prodavnica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pib', models.CharField(max_length=20)),
                ('naziv', models.CharField(max_length=50)),
                ('adresa', models.CharField(max_length=40)),
                ('broj_telefona', models.CharField(max_length=30, verbose_name='broj telefona')),
            ],
        ),
        migrations.AddField(
            model_name='artikal',
            name='kategorije',
            field=models.ManyToManyField(to='d3_primeri.Kategorija'),
        ),
        migrations.AddField(
            model_name='artikal',
            name='prodavnica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artikli', to='d3_primeri.Prodavnica'),
        ),
    ]
