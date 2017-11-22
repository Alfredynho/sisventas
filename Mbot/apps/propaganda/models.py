from django.db import models

from django.utils.translation import ugettext_lazy as _
import datetime

class Propaganda(models.Model):
	
	nombre = models.CharField(
		max_length = 120,
		verbose_name = _('Nombre')
	)

	descripcion = models.TextField(
		verbose_name = _('Descripcion')
	)

	fecha_inicio = models.DateField()
	
	fecha_fin = models.DateField()

	url = models.URLField(
		verbose_name = _('URL Propaganda'),
		max_length = 500
	)

	habilitado = models.BooleanField(
		default = False,
		verbose_name = _('Habilitado')
	)

	def __str__(self):
		return self.nombre

	def estadofecha(self):
		hoy = datetime.date.today()
		dias = (self.fecha_fin - hoy).days
		return dias

	class Meta:
		verbose_name = _('Propaganda')
		verbose_name_plural = _('Propagandas')