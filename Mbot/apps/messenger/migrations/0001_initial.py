# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessengerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messenger_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Messenger ID')),
                ('nombre', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=150, null=True, verbose_name='Apellido')),
                ('foto_perfil', models.CharField(blank=True, max_length=150, null=True, verbose_name='Foto de Perfil')),
                ('lugar', models.CharField(blank=True, max_length=150, null=True, verbose_name='Lugar')),
                ('zona_horaria', models.CharField(blank=True, max_length=150, null=True, verbose_name='Zona Horaria')),
                ('genero', models.CharField(blank=True, max_length=150, null=True, verbose_name='Género')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
                'verbose_name': 'Usuario',
            },
        ),
    ]
