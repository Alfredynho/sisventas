# -*- encoding: utf-8 -*-

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render_to_response as render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.utils import timezone
from django.shortcuts import render

from django.db import transaction, connection
from django.contrib import messages
from django.template import RequestContext as ctx
from django.core import serializers
from django.http import HttpResponseRedirect
from django import http
from django.template.loader import get_template
from django.template import Context

import json

from apps.reparacion.models import Asistencia
from datetime import datetime
from .forms import AsistenciaForm

from apps.cliente.models import Cliente
from apps.producto.models import Producto
from apps.empleado.models import Empleado
from apps.repuesto.models import Repuesto


from datetime import *
import datetime
import time


def crearAsistencia(request):
    form = None

    if request.method == 'POST':
        sid = transaction.savepoint()
        try:
            proceso = json.loads(request.POST.get('proceso'))
            print("El proceso ",proceso)

            if 'clienProv' not in proceso:
                msg = 'El cliente no ha sido seleccionado'
                raise Exception(msg)

            if len(proceso['producto']) <= 0:
                msg = 'No se ha seleccionado ningun producto'
                raise Exception(msg)

            total = 0

            for k in proceso['producto']:
                producto = Producto.objects.get(id=k['serial'])
                subTotal = (producto.precio_venta) * int(k['cantidad'])
                total += subTotal * 13
                total = total

            crearFactura = Venta(
                cliente=Cliente.objects.get(id=proceso['clienProv']),
                fecha=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                total=total,
                iva = subTotal,
                vendedor=request.user
            )

            crearFactura.save()
            print("Factura guardado")
            print(crearFactura.id)
            for k in proceso['producto']:
                producto = Producto.objects.get(id=k['serial'])
                crearDetalle = DetalleVenta(
                    producto=producto,
                    precio = producto.precio_venta,
                    cantidad=int(k['cantidad']),
                    subtotal=producto.precio_venta * int(k['cantidad']),
                    factura = crearFactura,
                    )
                crearDetalle.save()

            messages.success(
                request, 'La venta se ha realizado satisfactoriamente')
        except Exception as e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.error(request, e)

    context = {'form':form}

    print("El context >> ", context)

    return render(
        request,
        'asistencia/crear_asistencia.html',
        context,
        )



def buscarRepuesto(request):
    idRepuesto = request.GET['id']
    repuesto = Repuesto.objects.filter(numero_serie__contains=idRepuesto)
    print("ingresando a buscar ")

    data = serializers.serialize(
        'json', repuesto, fields=('numero_serie','color', 'nombre','cantidad', 'habilitado', 'precio_venta'))

    return HttpResponse(data, content_type='application/json')


class ListViewAsistencia(ListView):
	context_object_name = 'listar_asistencia'
	model = Asistencia
	template_name = 'asistencia/lista_asistencias.html'


class DetalleAsistenciaView(DetailView):
	model = Asistencia
	template_name = 'asistencia/detalle_asistencia.html'

class ActualizarAsistenciaView(UpdateView):
	form_class = AsistenciaForm
	template_name = 'asistencia/update_asistencia.html'
	model = Asistencia
	success_url='/listar_asitencia'


class EliminarAsistenciaView(DeleteView):
	model = Asistencia
	template_name = 'asistencia/eliminar_asistencia.html'
	success_url='/listar_asitencia'
