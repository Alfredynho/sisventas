# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-10 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usmbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chiste',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='consejomecanica',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
    ]
