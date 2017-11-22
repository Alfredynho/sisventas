from django.contrib import admin

from .models import Propaganda

@admin.register(Propaganda)

class PropagandaAdmin(admin.ModelAdmin):
	list_display = ['nombre' , 'descripcion', 'fecha_inicio','fecha_fin','url', 'habilitado']
	search_fields = ('nombre',)