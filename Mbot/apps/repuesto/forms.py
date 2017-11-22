from django import forms
from .models import Repuesto

class RepuestoForm(forms.ModelForm):
	class Meta:
		model = Repuesto
		exclude = ('marca',)
		fields = "__all__"