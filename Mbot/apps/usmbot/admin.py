from django.contrib import admin
from apps.usmbot.models import Chiste, ConsejoMecanica


@admin.register(Chiste)
class AdminChiste(admin.ModelAdmin):
	list_display = ('titulo','descripcion','habilitado')


@admin.register(ConsejoMecanica)
class AdminConsejoMecanica(admin.ModelAdmin):
	list_display = ('titulo','descripcion','habilitado')

