# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20170808_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='iva',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6),
        ),
    ]
