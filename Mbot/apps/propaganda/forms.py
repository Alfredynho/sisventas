# -*- encoding: utf-8 -*-

from django import forms
from .models import Propaganda

class CrearPropagandaForm(forms.ModelForm):
	class Meta:
		model = Propaganda
		exclude = ('',)

		widgets = {
				'nombre': forms.TextInput(attrs={'class': 'form-control'}),
				'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '6' }),
				'fecha_inicio': forms.DateInput(attrs={'class':'form-control', 'id':'Date', 'data-date-format':'dd/mm/yyyy'}),
				'fecha_fin': forms.DateInput(attrs={'class':'form-control', 'id':'Date1', 'data-date-format':'dd/mm/yyyy'}),
				'url': forms.TextInput(attrs={'class': 'form-control'}),
			}