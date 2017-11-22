# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-24 14:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='apellidos',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Apellido'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(default=datetime.datetime(2017, 10, 24, 14, 24, 29, 286078, tzinfo=utc), max_length=100, verbose_name='Nombre'),
            preserve_default=False,
        ),
    ]
