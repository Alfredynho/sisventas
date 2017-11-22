# -*- encoding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Propaganda
from .forms import CrearPropagandaForm

#reporte pdf
from django.http import HttpResponseRedirect, HttpResponse
from datetime import *
import xhtml2pdf.pisa as pisa
from django import http
from django.template.loader import get_template
from django.template import Context
from io import BytesIO as StringIO
import cgi

class ListaPropagandas(ListView):
	model = Propaganda
	context_object_name = 'lista_propagandas'
	template_name = 'chatbot/propagandas/listar_propagandas.html'


class DetalleView(DetailView):
	model = Propaganda
	template_name = 'chatbot/propagandas/detalle_propaganda.html'


class ActualizarView(UpdateView):
	form_class = CrearPropagandaForm
	template_name = 'chatbot/propagandas/update_propaganda.html'
	model = Propaganda
	success_url = '/propagandas'

class CreatePropagandas(CreateView):
	form_class = CrearPropagandaForm
	template_name = 'chatbot/propagandas/create_propaganda.html'
	model = Propaganda
	success_url = '/propagandas'


class EliminarView(DeleteView):
	model = Propaganda
	template_name = 'chatbot/propagandas/eliminar_propaganda.html'
	success_url = '/propagandas'



def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = StringIO()
    pdf = pisa.pisaDocument(StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


def generar_reporte_propagandas(request):
	 propagandas = Propaganda.objects.all()

	 return write_pdf ('chatbot/propagandas/reporte_detalle_propagandas.html',{'pagesize' : 'legal',
	 				   'propagandas' : propagandas})