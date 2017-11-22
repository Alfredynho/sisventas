#encoding:utf-8
from django import forms
from .models import Chiste, ConsejoMecanica

class CrearChisteForm(forms.ModelForm):
	class Meta:
		model = Chiste
		exclude = ('',)
		fields = "__all__"



class CrearConsejoMecanicaForm(forms.ModelForm):
	class Meta:
		model = ConsejoMecanica
		exclude = ('',)
		fields = "__all__"
