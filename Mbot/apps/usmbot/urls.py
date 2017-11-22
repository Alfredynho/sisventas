from django.conf.urls import include, url

from .views import (
	# URL Chistes
	ListarChistes,
	DetalleViewChiste,
	ActualizarViewChiste,
	CreateChiste,
	EliminarViewChiste,

	# URL Mecanica
	ListarConsejoMecanica,
	DetalleViewConsejoMecanica,
	ActualizarViewConsejoMecanica,
	CreateConsejoMecanica,
	EliminarViewConsejoMecanica

	)

urlpatterns =[
	# url chistes
	url(r'^listar_chistes/$', ListarChistes.as_view(), name = 'lista_chiste'),
	url(r'^chistes/detalle/(?P<pk>\d+)/$', DetalleViewChiste.as_view(),name='detalle_chiste'),
	url(r'^chistes/actualizar/(?P<pk>\d+)/$', ActualizarViewChiste.as_view(), name ="actualizar_chiste"),
	url(r'^chistes/agregar$', CreateChiste.as_view(), name='crear_chiste'),
	url(r'^chistes/eliminar/(?P<pk>\d+)/$', EliminarViewChiste.as_view(), name="eliminar_chiste"), 

	#url consejos mecanica
	url(r'^listar_consejos_mecanica/$', ListarConsejoMecanica.as_view(), name = 'lista_consejos'),
	url(r'^mecanica/detalle/(?P<pk>\d+)/$', DetalleViewConsejoMecanica.as_view(),name='detalle_mecanica'),
	url(r'^mecanica/actualizar/(?P<pk>\d+)/$', ActualizarViewConsejoMecanica.as_view(), name ="actualizar_mecanica"),
	url(r'^mecanica/agregar$', CreateConsejoMecanica.as_view(), name='crear_mecanica'),
	url(r'^mecanica/eliminar/(?P<pk>\d+)/$', EliminarViewConsejoMecanica.as_view(), name="eliminar_mecanica"), 

]