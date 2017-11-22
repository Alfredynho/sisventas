from django.shortcuts import render
from .forms import CrearChisteForm,CrearConsejoMecanicaForm
from django.views.generic import (
	ListView,
	DetailView,
	DeleteView,
	CreateView,
	UpdateView
	)
from .models import Chiste, ConsejoMecanica

# CRUD CHISTES
class ListarChistes(ListView):
	model = Chiste
	context_object_name = 'lista_chistes'
	template_name = 'chatbot/chistes/listar_chistes.html'

class DetalleViewChiste(DetailView):
	model = Chiste
	template_name = 'chatbot/chistes/detalle_chiste.html'

class ActualizarViewChiste(UpdateView):
	form_class = CrearChisteForm
	template_name = 'chatbot/chistes/update_chiste.html'
	model = Chiste
	success_url = '/listar_chistes'

class CreateChiste(CreateView):
	form_class = CrearChisteForm
	template_name = 'chatbot/chistes/create_chiste.html'
	model = Chiste
	success_url = '/listar_chistes'

class EliminarViewChiste(DeleteView):
	model = Chiste
	template_name = 'chatbot/chistes/eliminar_chiste.html'
	success_url = '/listar_chistes'


#CRUD CONSEJO MECANICA
class ListarConsejoMecanica(ListView):
	model = ConsejoMecanica
	context_object_name = 'lista_consejos'
	template_name = 'chatbot/mecanica/listar_mecanica.html'

class DetalleViewConsejoMecanica(DetailView):
	model = ConsejoMecanica
	template_name = 'chatbot/mecanica/detalle_mecanica.html'

class ActualizarViewConsejoMecanica(UpdateView):
	form_class = CrearConsejoMecanicaForm
	template_name = 'chatbot/mecanica/update_mecanica.html'
	model = ConsejoMecanica
	success_url = '/listar_consejos_mecanica'

class CreateConsejoMecanica(CreateView):
	form_class = CrearConsejoMecanicaForm
	template_name = 'chatbot/mecanica/create_mecanica.html'
	model = ConsejoMecanica
	success_url = '/listar_consejos_mecanica'

class EliminarViewConsejoMecanica(DeleteView):
	model = ConsejoMecanica
	template_name = 'chatbot/mecanica/eliminar_mecanica.html'
	success_url = '/listar_consejos_mecanica'