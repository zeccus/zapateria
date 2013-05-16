from principal.models import Empleados,Almacen,Zapato,Series,Genero,Color,Marca,Persona,Cabecera,Detalle,Tipo
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from util import decoradores

def lista_zapatos(request):
    zapatos = Zapato.objects.all()
    series = Series.objects.all()
    context_instance=RequestContext(request)
    return render_to_response('inicio.html',{'lista':zapatos,'series':series},context_instance)

def lista_proovedores(request):
    proovedores = Persona.objects.filter(proovedor = True).values()
    context_instance=RequestContext(request)
    return render_to_response('proovedor.html',{'proovedores': proovedores},context_instance)

#render_with('productos.html')
def zapato_especifico(request,id_zapato):
	dato = get_object_or_404(Zapato, pk=id_zapato)
	datos_zapato = Series.objects.filter(zapato = dato)
	context_instance=RequestContext(request)
	return render_to_response('producto.html',{'dato':dato,'datos_zapato':datos_zapato},context_instance)

def zapato_nino(request):
	nino = Zapato.objects.filter(genero = 1)
	context_instance = RequestContext(request)
	return render_to_response('ninos.html',{'nino':nino},context_instance)
	
def zapato_nina(request):
	nina = Zapato.objects.filter(genero = 2)
	context_instance = RequestContext(request)
	return render_to_response('ninas.html',{'nina':nina},context_instance)
	
def zapato_unisex(request):
	uni = Zapato.objects.filter(genero = 3)
	context_instance = RequestContext(request)
	return render_to_response('unisex.html',{'uni':uni},context_instance)
	
def marca(request):
	marca = Marca.objects.all()
	context_instance = RequestContext(request)
	return render_to_response('marcas.html',{'marca':marca},context_instance)

def zapato_marca(request, id_marca):
	dato = get_object_or_404(Marca, pk=id_marca)
	zapato = Zapato.objects.filter(marca = dato)
	context_instance = RequestContext(request)
	return render_to_response('producto_marca.html',{'dato':dato, 'zapato':zapato},context_instance)

def tipo(request):
	tipo = Tipo.objects.all()
	context_instance = RequestContext(request)
	return render_to_response('tipo.html',{'tipo':tipo},context_instance)

def tipo_zapato (request, id_tipo):
	dato = get_object_or_404(Tipo, pk=id_tipo)
	zapato = Zapato.objects.filter (tipo = dato)
	context_instance = RequestContext(request)
	return render_to_response('productos_tipo.html',{'dato':dato,'zapato':zapato},context_instance)
