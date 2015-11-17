# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre_provincia = models.CharField(max_length=50, blank=True)
    descripcion_provincia = models.TextField(blank=True)
    region = models.CharField(max_length=10)
    foto_provincia = models.CharField(max_length=250)

     
    class Meta:
        managed = False
        db_table = 'provincia'

    def __unicode__(self):
        return "%s"%(self.nombre_provincia)    

    def __str__(self):
        return "%s"%(self.nombre_provincia)

class CatalogoServicios(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    nombre_servicio = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'catalogo_servicios'


class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    id_provincia = models.ForeignKey('Provincia', db_column='id_provincia')
    nombre_ciudad = models.CharField(max_length=50, blank=True)    
    
    class Meta:
        managed = False
        db_table = 'ciudad'


    def __unicode__(self):
        return "%s"%(self.nombre_ciudad)


class Hotel(models.Model):
    id_hotel = models.IntegerField(primary_key=True)
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad')
    nombre_hotel = models.TextField(blank=True)
    descripcion_hotel = models.TextField(blank=True)
    tarjeta_hotel = models.TextField(blank=True)
    ubicacion_hotel = models.TextField(blank=True)
    direccion_hotel = models.TextField(blank=True)
    web_hotel = models.CharField(max_length=35, blank=True)
    clasificacion_hotel = models.IntegerField(blank=True, null=True)
    foto_hotel = models.CharField(max_length=254, blank=True)
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hotel'


    def __unicode__(self):
        return "%s"%(self.nombre_hotel)



class Contacto(models.Model):
    id_contactos = models.IntegerField(primary_key=True)
    id_hotel = models.ForeignKey('Hotel', db_column='id_hotel')
    telefono_hotel = models.CharField(max_length=40, blank=True)
    fax_hotel = models.CharField(max_length=20, blank=True)
    correo_hotel = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'contacto'


class Fotos(models.Model):
    id_foto = models.IntegerField(primary_key=True)
    id_hotel = models.ForeignKey('Hotel', db_column='id_hotel', blank=True, null=True)
    foto = models.CharField(max_length=254, blank=True)

    class Meta:
        managed = False
        db_table = 'fotos'


class Habitacion(models.Model):
    id_habitacion = models.IntegerField(primary_key=True)
    id_hotel = models.ForeignKey('Hotel', db_column='id_hotel')
    tipo_habitacion = models.CharField(max_length=65535, blank=True)
    tarifa_sencilla = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    tarifa_doble = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    tarifa_triple = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habitacion'




class Promocion(models.Model):
    id_promocion = models.IntegerField(primary_key=True)
    id_hotel = models.ForeignKey(Hotel, db_column='id_hotel', blank=True, null=True)
    descripcion_promocion = models.TextField(blank=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promocion'



class Servicios(models.Model):
    id_servicios = models.IntegerField(primary_key=True)
    id_hotel = models.ForeignKey(Hotel, db_column='id_hotel')
    id_servicio = models.ForeignKey(CatalogoServicios, db_column='id_servicio')
    estado = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'servicios'


