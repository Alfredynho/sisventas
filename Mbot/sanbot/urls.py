from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from django.contrib.auth.views import (
        login, 
        logout_then_login, 
        password_reset, 
        password_reset_done, 
        password_reset_confirm, 
        password_reset_complete
    )


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('apps.inicio.urls',namespace='inicio')),
    url(r'^accounts/login/', login, {'template_name':'users/login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),

    url(r'^integrations/', include('apps.messenger.urls', namespace="integrations")),
    url(r'', include('apps.proveedor.urls',namespace='proveedor')),
    url(r'', include('apps.cliente.urls',namespace='clientes_app')),
    url(r'', include('apps.producto.urls',namespace='productos')),
    url(r'', include('apps.empleado.urls',namespace='empleados')),
    url(r'', include('apps.venta.urls',namespace='ventas')),
    url(r'', include('apps.repuesto.urls',namespace='repuestos')),
    url(r'', include('apps.propaganda.urls',namespace='propagandas')),
    url(r'', include('apps.reparacion.urls',namespace='reparaciones')),
    url(r'', include('apps.usmbot.urls',namespace='usmbot')),
    url(r'', include('apps.graficos.urls',namespace='graficos')),

    # URL APPS PROJECT 

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),

]	