# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0004_detalleventa_iva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleventa',
            name='iva',
        ),
        migrations.AddField(
            model_name='venta',
            name='iva',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6),
        ),
    ]
