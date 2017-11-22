from django.shortcuts import render
from django.views.generic import View

class GraphicProveedor(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts/charts_proveedores.html')

class GraphicVentaProductos(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts/charts_venta_productos.html')

class GraphicVentaMes(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'charts/charts_venta_mes.html')