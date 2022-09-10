from cProfile import label
from pyexpat import model
from django import forms
from .models import Comentario

class FormComment(forms.Form):
	model = Comentario
	fields = ('cuerpo_comentario')

	cuerpo_comentario = forms.CharField(label='Escribenos tu comentario',widget=forms.Textarea)

