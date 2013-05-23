#encoding:utf-8
from django.forms import ModelForm
from django import forms

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Correo Electronico')
	mensaje = forms.CharField(widget=forms.Textarea)