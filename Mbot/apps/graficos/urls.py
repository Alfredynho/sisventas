from django.conf.urls import url
from django.contrib import admin

from .views import GraphicProveedor, GraphicVentaProductos, GraphicVentaMes
from .endpoint import (
	ChartProveedores, 
	ChartVentaProductos, 
	ChartVentaProductosMes	
	)


urlpatterns = [
    url(r'^proveedores_usados/$', GraphicProveedor.as_view(), name='graphic_proveedores'),
    url(r'^productos_usados/$', GraphicVentaProductos.as_view(), name='graphic_productos'),
    url(r'^ventas_mes/$', GraphicVentaMes.as_view(), name='graphic_mes'),
    url(r'^api/chart/proveedores/$', ChartProveedores.as_view()),
    url(r'^api/chart/productos/$', ChartVentaProductos.as_view()),
    url(r'^api/chart/ventas/$', ChartVentaProductosMes.as_view()),
]
