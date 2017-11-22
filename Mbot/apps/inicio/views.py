from django.views.generic import ListView
from apps.producto.models import Producto
from apps.venta.models import Venta
from apps.empleado.models import Empleado
from apps.proveedor.models import Proveedor

class HomeView(ListView):
	context_object_name = 'productos'
	model = Producto
	template_name = "dashboard.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['cantidad_productos'] = Producto.objects.count()
		context['cantidad_ventas'] = Venta.objects.count()
		context['cantidad_personal'] = Empleado.objects.count()
		context['cantidad_proveedores'] = Proveedor.objects.count()
		return context