from django.conf.urls import url
from .views import (
	ListaProductos,
	DetalleView,
	ActualizarView,
	ModificarView,
	CreateProductos,
	EliminarView,
	generar_reporte_productos,

	# inventario
	ProductoSucursalListView,
	ProductosListSucursal,
	BusquedaProductoView,
	BusquedaAjaxView
)

urlpatterns = [

	url(r'^productos/$', ListaProductos.as_view(), name = 'lista_productos'),
	url(r'^productos/detalle/(?P<pk>\d+)/$', DetalleView.as_view(),name='detalle_productos'),
	url(r'^productos/actualizar/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_productos"),
	url(r'^productos/modificar/(?P<pk>\d+)/$', ModificarView.as_view(), name ="modificar_productos"),
	url(r'^productos/agregar$', CreateProductos.as_view(), name='crear_productos'),
	url(r'^productos/eliminar/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_productos"),
	url(r'^productos/reporte/$', generar_reporte_productos,name='reporte'),

	url(r'^productos/sucursal/(?P<pk>\d+)/$', ProductoSucursalListView.as_view(), name='listar-productos-sucursal'),

	url(r'^productos/inventario$', ProductosListSucursal.as_view(), name='listar-productos-inventario'),
	url(r'^productos/lista$', BusquedaProductoView.as_view(), name='listar-productos'),
	url(r'^productos/busqueda_producto/$', BusquedaAjaxView.as_view(), name='busqueda-productos'),
	]
