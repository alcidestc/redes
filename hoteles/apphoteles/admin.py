from django.contrib import admin
from apphoteles.models import *

# Register your models here.



#en vez de * puede ir los mombres de cada entidad separadas por coma

class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ('id_provincia','nombre_provincia', 'descripcion_provincia', 'region', 'foto_provincia')

class CatalogoServiciosAdmin(admin.ModelAdmin):
	list_display = ('id_servicio','nombre_servicio')


class CiudadAdmin(admin.ModelAdmin):
	list_display = ('id_ciudad','id_provincia','nombre_ciudad')

class ContactoAdmin(admin.ModelAdmin):
	list_display = ('id_hotel','telefono_hotel','fax_hotel','correo_hotel')	

class FotosAdmin(admin.ModelAdmin):
	list_display = ('id_foto', 'id_hotel', 'foto')	
		


class HabitacionAdmin(admin.ModelAdmin):
	list_display = ('id_habitacion','id_hotel','tipo_habitacion','tarifa_sencilla', 'tarifa_doble','tarifa_triple')

class HotelAdmin(admin.ModelAdmin):
	list_display = ('id_hotel','id_ciudad','nombre_hotel','descripcion_hotel', 'tarjeta_hotel','ubicacion_hotel', 'direccion_hotel', 'web_hotel', 'clasificacion_hotel', 'foto_hotel', 'latitud', 'longitud')	


class PromocionAdmin(admin.ModelAdmin):
	list_display = ('id_promocion', 'id_hotel','descripcion_promocion','fecha_inicio','fecha_fin')


class ServiciosHotelAdmin(admin.ModelAdmin):
	list_display = ('id_hotel','id_servicio', 'estado')


admin.site.register(CatalogoServicios, CatalogoServiciosAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Fotos, FotosAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Promocion, PromocionAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Servicios, ServiciosHotelAdmin)