from django.conf.urls import patterns, include, url
from django.contrib import admin
from apphoteles.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hoteles.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'apphoteles.views.inicio', name='inicio'),
    url(r'^ciudades/(?P<id_provincia>\d+)/$', 'apphoteles.views.ciudades', name='ciudades'),
    url(r'^provincias/(.+)/$', 'apphoteles.views.provincias', name='provincias'),
    url(r'^hotel/(?P<id_hotel>\d+)/$', 'apphoteles.views.hotel', name='hotel'),
    url(r'^hoteles/(?P<id_ciudad>\d+)/$', 'apphoteles.views.hoteles', name='hoteles'),
    url(r'^hotelesEstrellas/(\d+)/$', 'apphoteles.views.hotelesEstrellas', name='hotelesEstrellas'),
    url(r'^mapas/', 'apphoteles.views.mapas', name='mapas'),
    
    
   
    # url(r'^productos/', 'portal.views.productos', name='productos'),    
)
