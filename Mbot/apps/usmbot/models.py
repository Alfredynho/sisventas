from django.db import models
from django.utils.translation import ugettext_lazy as _

class Chiste(models.Model):

	titulo = models.CharField(
		verbose_name= _('Titulo'),
		max_length=100
	)

	descripcion = models.TextField(
		verbose_name=_('Descripcion'),
		blank=True,
		null=True
	)

	habilitado = models.BooleanField(
		verbose_name=_('Habilitado'),
		default = False
	)

	def __str__(self):
		return str(self.titulo)


class ConsejoMecanica(models.Model):

	titulo = models.CharField(
		verbose_name= _('Titulo'),
		max_length=100
	)

	descripcion = models.TextField(
		verbose_name=_('Descripcion'),
		blank=True,
		null=True
	)

	habilitado = models.BooleanField(
		verbose_name=_('Habilitado'),
		default = False
	)


	def __str__(self):
		return str(self.titulo)