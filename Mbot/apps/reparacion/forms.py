# -*- encoding: utf-8 -*-
from django import forms

from apps.reparacion.models import Asistencia

class AsistenciaForm(forms.ModelForm):
	class Meta:
		model = Asistencia
		exclude = ()
		widgets = {
				'empleado': forms.Select(attrs={'class': 'form-control'}),
				'cliente': forms.Select(attrs={'class': 'form-control'}),
				'motocicleta': forms.Select(attrs={'class': 'form-control'}),
				'placa': forms.TextInput(attrs={'class': 'form-control'}),
				'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '6' }),
				'fecha_entrada': forms.DateInput(attrs={'class':'form-control', 'id':'Date', 'data-date-format':'dd/mm/yyyy'}),
				'fecha_salida': forms.DateInput(attrs={'class':'form-control', 'id':'Date1', 'data-date-format':'dd/mm/yyyy'}),
				'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows': '6' }),
				'total': forms.NumberInput(attrs={'class': 'form-control', 'id':'precio_venta'}),
				'habilitado': forms.NumberInput(attrs={'class': 'form-control', 'id':'igv'}),
			}