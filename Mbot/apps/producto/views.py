# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy
from django.core import serializers
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from apps.producto.models import Producto

from .forms import ProductoForm, CrearProductoForm
from django.http import HttpResponse, Http404
import csv

#reporte pdf
from django.http import HttpResponseRedirect, HttpResponse
from datetime import *
import xhtml2pdf.pisa as pisa
from django import http
from django.template.loader import get_template
from django.template import Context
from io import BytesIO as StringIO
import cgi


class ListaProductos(ListView):
	context_object_name = 'productos'
	model = Producto
	template_name = 'productos/lista_productos.html'


	def get_context_data(self, **kwargs):
		context = super(ListaProductos, self).get_context_data(**kwargs)
		context['cantidad'] = Producto.objects.filter(habilitado__contains='true').count()
		return context

class DetalleView(DetailView):
	model = Producto
	template_name = 'productos/detalle_productos.html'

class ActualizarView(UpdateView):
	form_class = ProductoForm
	template_name = 'productos/create_update_productos.html'
	model = Producto
	success_url='/productos'

class ModificarView(UpdateView):
	form_class = ProductoForm
	template_name = 'productos/create_update_productos.html'
	model = Producto
	success_url='/productos/lista'

class CreateProductos(CreateView):
	form_class = CrearProductoForm
	template_name = 'productos/create_productos.html'
	model = Producto
	success_url = '/productos'

class EliminarView(DeleteView):
	model = Producto
	template_name = 'productos/eliminar_producto.html'
	success_url='/productos'

def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = StringIO()
    pdf = pisa.pisaDocument(StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


def generar_reporte_productos(request):
	 productos = Producto.objects.all()

	 return write_pdf ('productos/reporte_detalle_productos.html',{'pagesize' : 'legal',
	 				   'productos' : productos})


class ProductoSucursalListView(ListView): 
	
	context_object_name = 'sucursal_productos'
	template_name = 'inventario/inventario_list_productos.html'

	def get_queryset(self):


		sucursal_id = self.kwargs['pk']
		sucursal = Sucursal.objects.get(id=sucursal_id)
		
		sucursal_productos = SucursalProducto.objects.filter(sucursal=sucursal)
		return sucursal_productos

	def get_context_data(self,**kwargs):

		context = super(ProductoSucursalListView,self).get_context_data(**kwargs)
		sucursal_id = self.kwargs['pk']
		sucursal = Sucursal.objects.get(id=sucursal_id)
		context['sucursal'] = sucursal
		context['productos'] = Producto.objects.all()
		
		return context

class ProductosListSucursal(ListView):

	model = Producto
	context_object_name = 'sucursal_motocicletas'
	template_name = 'inventario/inventario_sucursal_producto.html'


class BusquedaProductoView(ListView):
	model = Producto
	template_name = 'productos/productos.html'
	context_object_name = 'productos'


	def get_context_data(self, **kwargs):
		context = super(BusquedaProductoView, self).get_context_data(**kwargs)
		context['naked'] = Producto.objects.filter(habilitado__contains='true', tipo__contains='Naked').count() 
		context['scooter'] = Producto.objects.filter(habilitado__contains='true', tipo__contains='Scooter').count() 
		context['urbana'] = Producto.objects.filter(habilitado__contains='true', tipo__contains='Urbana').count() 
		context['trabajo'] = Producto.objects.filter(habilitado__contains='true', tipo__contains='Trabajo').count() 
		context['touring'] = Producto.objects.filter(habilitado__contains='true', tipo__contains='Touring').count() 
		context['crucero'] = Producto.objects.filter(habilitado__contains='true', tipo__contains='Crucero').count() 
		context['cross'] = Producto.objects.filter(habilitado__contains='true', tipo__contains='Cross').count() 
		context['atv'] = Producto.objects.filter(habilitado__contains='true', tipo__contains='atv').count() 
		context['deportiva'] = Producto.objects.filter(habilitado__contains='true', tipo__contains='Deportiva').count() 
		context['accesorio'] = Producto.objects.filter(habilitado__contains='true', tipo__contains='Accesorio').count() 
		return context


class BusquedaAjaxView(TemplateView):
	def get(self, request,*args, **kwargs):
		id_producto = request.GET['id']

		productos = Producto.objects.filter(tipo =id_producto, habilitado__contains='true')
		data = serializers.serialize('json',productos,
			fields=('id','numero_serie','nombre','marca','color','habilitado', 'tipo'))
		return HttpResponse(data,content_type='application/json')