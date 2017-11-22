# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .views import (
	ListaPropagandas, 
	DetalleView,
	ActualizarView,
	CreatePropagandas,
	EliminarView,
	generar_reporte_propagandas
	)

urlpatterns = [

	url(r'^propagandas/$', ListaPropagandas.as_view(), name = 'lista_propagandas'),
	url(r'^propagandas/detalle/(?P<pk>\d+)/$', DetalleView.as_view(),name='detalle_propaganda'),
	url(r'^propagandas/actualizar/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_propaganda"),
	url(r'^propagandas/reporte/$', generar_reporte_propagandas,name='reporte'),
	url(r'^propagandas/agregar$', CreatePropagandas.as_view(), name='crear_propaganda'),
	url(r'^propagandas/eliminar/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_propaganda"), 
	]
