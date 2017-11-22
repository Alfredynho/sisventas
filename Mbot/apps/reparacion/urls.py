# -*- encoding: utf-8 -*-

from django.conf.urls import url
from .views import (
	ListViewAsistencia, 
	buscarRepuesto,
	crearAsistencia,
	DetalleAsistenciaView, 
	ActualizarAsistenciaView, 
	EliminarAsistenciaView
)

urlpatterns = [
	url(r'^listar_asitencia/$',ListViewAsistencia.as_view(),name='listar_asistencia'),
	url(r'^crear_asistencia/$',crearAsistencia,name='crear_asistencia'),
    url(r'^asistencia/buscar_repuesto/$', buscarRepuesto, name = 'buscar_repuesto'),
]
