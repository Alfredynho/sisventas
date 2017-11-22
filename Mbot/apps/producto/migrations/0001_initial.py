# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 01:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_serie', models.CharField(help_text='Ingresa el numero de serie ej. USM-1001', max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]{3}-[0-9]{4}', code='Invalid Key', message='Debe ingresar un codigo valido ej: USM-1001')], verbose_name='Numero Serie')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('marca', models.CharField(default='USM', max_length=100, verbose_name='Marca')),
                ('color', models.CharField(blank=True, max_length=20, null=True, verbose_name='Color')),
                ('cantidad', models.IntegerField(blank=True, null=True, verbose_name='Cantidad')),
                ('precio_compra', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Precio Compra')),
                ('precio_venta', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Precio Venta')),
                ('caracteristicas', models.TextField(blank=True, null=True, verbose_name='Caracteristicas')),
                ('tipo', models.CharField(choices=[('Scooter', 'Scooter'), ('Urbana', 'Urbana'), ('Trabajo', 'Trabajo'), ('Touring', 'Touring'), ('Crucero', 'Crucero'), ('Cross', 'Cross'), ('atv', 'Atv'), ('Deportiva', 'Deportiva'), ('Naked', 'Naked'), ('Accesorio', 'Accesorio')], default='Scooter', max_length=50, verbose_name='Tipo')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/productos/', verbose_name='Imagen')),
                ('habilitado', models.BooleanField(default=True, verbose_name='Habilitado')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.Proveedor', verbose_name='Proveedor')),
            ],
            options={
                'ordering': ['numero_serie'],
                'verbose_name_plural': 'Productos',
                'verbose_name': 'Producto',
            },
        ),
    ]