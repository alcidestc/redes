from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import Http404
from models import Provincia, Promocion, Hotel, Habitacion, Fotos, Contacto, Ciudad, Servicios, CatalogoServicios
# Create your views here.

# def inicio(request):
# 	return render_to_response('inicio.html', context_instance=RequestContext(request))



def inicio(request):
	# provincias = Provincia.objects.all()
	cities = Ciudad.objects.all()	

	# context = {'ciudades': ciudades, 'provincias':provincias}	    
	return render(request, 'inicio.html', {'cities': cities})

def ciudades(request, id_provincia):	
	try:
		provincia = Provincia.objects.get(pk=id_provincia)
		ciudades = Ciudad.objects.filter(id_provincia=id_provincia)						
		hoteles = Hotel.objects.all()


		#menu
		cities = Ciudad.objects.all()	
		
		
	except Hotel.DoesNotExist:
		raise Http404	
	return render(request, 'ciudades.html', {'ciudades': ciudades, 'provincia':provincia, 'hoteles':hoteles, 'cities':cities})


def hotel(request, id_hotel):	
	try:
		hotel = Hotel.objects.get(pk=id_hotel)
		contactos = Contacto.objects.filter(id_hotel=id_hotel)	
		habitaciones = Habitacion.objects.filter(id_hotel=id_hotel)
		promociones  = Promocion.objects.filter(id_hotel=id_hotel)
		servicios = Servicios.objects.filter(id_hotel=id_hotel)
		fotos = Fotos.objects.filter(id_hotel=id_hotel)

		for p in promociones:
			print p.descripcion_promocion
		
				
		#menu
		cities = Ciudad.objects.all()
	except Hotel.DoesNotExist:
		raise Http404	
	return render(request, 'hotel.html', {'hotel':hotel, 'contactos':contactos, 'habitaciones':habitaciones, 'promociones': promociones, 'cities': cities, 'servicios':servicios, 'fotos':fotos})


def hoteles(request, id_ciudad):	
	try:
		hoteles = Hotel.objects.filter(id_ciudad=id_ciudad)
		ciudad = Ciudad.objects.get(pk=id_ciudad)


		#menu
		cities = Ciudad.objects.all()
	except Hotel.DoesNotExist:
		raise Http404	
	return render(request, 'hoteles.html', {'hoteles':hoteles, 'cities': cities, 'ciudad': ciudad})


def hotelesEstrellas(request, categoria):	
	print int(categoria)
	try:
		hoteles = Hotel.objects.filter(clasificacion_hotel=categoria)		


		#menu
		cities = Ciudad.objects.all()
	except Hotel.DoesNotExist:
		raise Http404	
	return render(request, 'hotelesEstrellas.html', {'hotelesEstrellas':hoteles, 'cities': cities, 'categoria': categoria})


def mapas(request):	
	try:
		hoteles = Hotel.objects.all()


		#menu
		cities = Ciudad.objects.all()
	except Hotel.DoesNotExist:
		raise Http404
	return render(request, 'mapas.html', {'hoteles': hoteles, 'cities':cities})


def provincias(request, region):
	provincias = Provincia.objects.all()
	
	try:
		provincias = Provincia.objects.filter(region=region)


		#menu
		cities = Ciudad.objects.all()
		
	except Hotel.DoesNotExist:
		raise Http404	
	return render(request, 'provincias.html', {'provincias':provincias, 'cities':cities, 'region':region })




# def mapa(request):
# 	lugar = lugares.objects.all()
# 	return render_to_response('mapa.html', {'lugar':lugar})

# # Create your views here.



# def hora(request, tiempo1 ):
# 	try: 
# 		tiempo1=int (tiempo1)     	
# 	except ValueError:
# 		raise Http404()
# 	dt= datetime.datetime.now()+datetime.timedelta(hours=tiempo1)
# 	html = "<html><body><h1>En %s hora(s), seran:</h1> <h3>%s</h3></body></html>" % (tiempo1, dt) 
# 	return HttpResponse(html)