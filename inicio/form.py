from django import forms
from ckeditor.fields import RichTextFormField


class PerroFormularioBase(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    descripcion = RichTextFormField()


class CrearPerroFormulario(PerroFormularioBase):
    ...
    
class ModificarPerroFormulario(PerroFormularioBase):
    ...
    
class BuscarPerroFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)