#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Zapato, Marca, Persona

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Correo Electronico')
	mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')

class ZapatoForm(ModelForm):
	class Meta:
		model = Zapato

class MarcaForm(ModelForm):
	class Meta:
		model = Marca

