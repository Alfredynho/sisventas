from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Repuesto
from .forms import RepuestoForm

class CreateRepuestos(CreateView):
	form_class = RepuestoForm
	template_name = 'repuestos/create_repuestos.html'
	model = Repuesto
	success_url = '/repuestos'


class ListaRepuestos(ListView):
	model = Repuesto
	context_object_name = 'repuestos'
	template_name = 'repuestos/lista_repuestos.html'
