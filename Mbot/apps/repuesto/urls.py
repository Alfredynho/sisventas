from django.conf.urls import url
from .views import (
	ListaRepuestos,
	# DetalleView,
	# ActualizarView,
	CreateRepuestos
	# EliminarView,
	# generar_reporte_productos,

	# # inventario
	# ProductoSucursalListView,
	# ProductosListSucursal,
	# BusquedaProductoView,
	# BusquedaAjaxView
)

urlpatterns = [

	url(r'^repuestos/$', ListaRepuestos.as_view(), name = 'lista_repuestos'),
	# url(r'^productos/detalle/(?P<pk>\d+)/$', DetalleView.as_view(),name='detalle_productos'),
	# url(r'^productos/actualizar/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_productos"),
	url(r'^repuestos/agregar$', CreateRepuestos.as_view(), name='crear_repuestos'),
	# url(r'^productos/eliminar/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_productos"),
	# url(r'^productos/reporte/$', generar_reporte_productos,name='reporte'),

	# url(r'^productos/lista$', BusquedaProductoView.as_view(), name='listar-productos'),
	# url(r'^productos/busqueda_producto/$', BusquedaAjaxView.as_view(), name='busqueda-productos'),

	]
