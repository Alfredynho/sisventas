# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-24 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0002_auto_20170909_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='habilitado',
            field=models.BooleanField(default=False, verbose_name='Habilitado'),
        ),
    ]
