# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response as render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext

from django.utils import timezone
from django.shortcuts import render

from django.db import transaction, connection
from django.contrib import messages
from django.views.generic import ListView, TemplateView, CreateView, DetailView, View
from django.template import RequestContext as ctx
from django.core import serializers
from django import http
from django.template.loader import get_template
from django.template import Context
from django.db.models import Q, Count, Sum
from django.db.models.functions import Coalesce

from apps.cliente.models import Cliente
from apps.producto.models import Producto
from apps.empleado.models import Empleado
from apps.proveedor.models import Proveedor
from .models import Venta, DetalleVenta

from .forms import RangoForm

#Reporte pdf

import json
from datetime import *
import time
import datetime
import xhtml2pdf.pisa as pisa
from io import BytesIO as StringIO
import cgi


def ventaCrear(request):

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

    return render(
        request,
        'factura/crear_factura.html',
        context,
        )

        
def buscarCliente(request):

    cliente = Cliente.objects.filter(cedula__contains=request.GET['id'])
    data = serializers.serialize(
        'json', cliente, fields=('cedula', 'nombre', 'apellidos', 'celular'))
    return HttpResponse(data, content_type='application/json')


def buscarProducto(request):

    _lower_producto = request.GET['id']
    _lower_producto = _lower_producto.title()
      
    producto = Producto.objects.filter(Q(nombre__contains=request.GET['id']) | Q(nombre__contains=_lower_producto) | Q(numero_serie__contains=request.GET['id']) | Q(numero_serie__contains=_lower_producto) | Q(tipo__contains=request.GET['id']) | Q(tipo__contains=_lower_producto))

    data = serializers.serialize(
        'json', producto, fields=('numero_serie','color','producto', 'nombre','cantidad', 'habilitado', 'precio_venta', 'tipo'))
    
    return HttpResponse(data, content_type='application/json')


def consultarFactura(request):
    factura = None
    detalles = None
    sum_subtotal = 0
    sum_tax = 0
    if request.method == 'POST':
        serie = request.POST.get('serie')
        numero = request.POST.get('num')

        factura = Factura.objects.get(serie=serie, numero=numero)
        detalles = DetalleFactura.objects.filter(factura=factura)

        for d in detalles:

            sum_tax = sum_tax + d.impuesto
        sum_subtotal = factura.total-sum_tax

    return render_to_response('factura/imprimir_factura.html',
                              {'factura': factura, 'detalles': detalles,
                                  'sum_subtotal': sum_subtotal, 'sum_tax': sum_tax},
                              context_instance=RequestContext(request))


class ListaVentas(ListView):
    template_name = 'factura/lista_venta.html'
    model = Venta
    
    def get_context_data(self, **kwargs):
        context = super(ListaVentas, self).get_context_data(**kwargs)
        context['Ventas'] = Venta.objects.all()
        return context



def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO()
    pdf = pisa.pisaDocument(StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


def generar_pdf(request):
    factura = Venta.objects.all()

    if request.method == "POST":
        formbusqueda = RangoForm(request.POST)
        vendedor = request.POST.get('vendedor')
        
        if formbusqueda.is_valid():
            fecha_in = formbusqueda.cleaned_data['fecha_i']
            fecha_fi = formbusqueda.cleaned_data['fecha_f']
            rango = Venta.objects.filter(fecha__range=(fecha_in, fecha_fi)).filter(vendedor__pk=request.user.id)
          
            total = 0
            for expe in rango:
                total = ((expe.total) + (total))

            return write_pdf ('factura/reporte_factura.html',{'pagesize' : 'legal', 'rango' : rango, 'total': total})
            #return render_to_response ('empleados/test.html',{'rango':rango},context_instance=RequestContext(request))
        else:
            error = "Hay un error en las fechas proporcionadas"
            return render_to_response('factura/rango_reporte.html', {'error': error}, context_instance=RequestContext(request))
    return render(request,'factura/rango_reporte.html', {'rangoform': RangoForm()})
    

def reporteventas(request, pk):
    compra = Venta.objects.get(pk=pk)
    detalle_venta = compra.venta.all()
    hora = time.strftime("%H:%M:%S")

    context = {
                "compra":compra,
                "detalle_venta":detalle_venta,
                "hora": hora
              }

    return render(
        request,
        'factura/detalle_venta.html', 
        context
        )