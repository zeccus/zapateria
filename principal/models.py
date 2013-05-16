from django.db import models
from django.contrib.auth.models import User

class Empleados(models.Model):
    Telefono = models.TextField(verbose_name='Telefono Empleado')
    usuario = models.OneToOneField(User)
    def __unicode__ (self):
        return unicode(self.usuario)

class Almacen(models.Model):
    empleados = models.ManyToManyField(Empleados)
    direccion = models.TextField(verbose_name='Direccion')
    telefono = models.TextField(verbose_name='Telefono')
    def __unicode__ (self):
        return self.direccion

class Zapato(models.Model):
    color = models.ManyToManyField("Color")
    genero = models.ForeignKey("Genero")
    marca = models.ForeignKey("Marca")
    tipo = models.TextField()
    descripcion = models.TextField(help_text="descripcion del zapato")
    imagen = models.ImageField(upload_to = 'zapateria/media/')
    def __unicode__(self):
        return self.tipo

class Series(models.Model):
    minymax = models.TextField()
    pvp = models.DecimalField(max_digits = 5,decimal_places = 2)
    numeroseries = models.ManyToManyField("numeroSeries")
    zapato = models.ManyToManyField("Zapato")
    def __unicode__(self):
        return self.minymax

class numeroSeries(models.Model):
    numero = models.IntegerField()
    cantidadPorNumero = models.IntegerField()
    almacen = models.ManyToManyField(Almacen)
  #  def __unicode__(self):
   #     return self.numero
    
class Genero(models.Model):
    genero = models.TextField()
    def __unicode__(self):
        return self.genero

class Color(models.Model):
    nombre = models.TextField()
    codColor = models.TextField()
    def __unicode__(self):
        return self.nombre

class Marca(models.Model):
    persona = models.ForeignKey("Persona")
    nombre = models.TextField()
    imagen = models.ImageField(upload_to = 'zapateria/media/')
    def __unicode__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.TextField(verbose_name='Nombre Persona o Entidad')
    direccion = models.TextField()
    telf = models.TextField()
    telf_viajante = models.TextField()
    correo = models.EmailField(null = True)
    proovedor = models.BooleanField(verbose_name='Marcar si es Proovedor')
    NifDNI = models.CharField(max_length = 10,verbose_name='NIF o DNI')
    def __unicode__(self):
        return self.nombre

class Cabecera(models.Model):
    persona = models.ManyToManyField(Persona)
    fecha = models.DateTimeField()
  #  def __unicode__(self):
   #     return self.fecha

class Detalle(models.Model):
    cabecera = models.ForeignKey(Cabecera)
    zapato = models.ForeignKey(Zapato)
    numeroVendido = models.IntegerField()
    cantidadVendida = models.IntegerField()
    #def __unicode__(self):
     #   return self.numproduc

