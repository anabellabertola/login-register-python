from typing import Any, Dict
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Perro
from django.shortcuts import render, redirect
from inicio.form import CrearPerroFormulario, BuscarPerroFormulario, ModificarPerroFormulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#v1

#def inicio(request):
 #   return HttpResponse('Hola soy tu inicio')

#v2
#def inicio(resquest):
 #   archivo = open(r'C:\Users\anabe\OneDrive\Escritorio\Mi_primer_django\templates\inicio.html', 'r')
  #  
   # template = Template(archivo.read())
    #
   # archivo.close()
   # 
  #  segundos = datetime.now().second
   # 
   # diccionario = {
    #    'mensaje': 'Este es el mensaje de inicio...',
     #   'segundos': segundos,
       #  'segundo_par': segundos%2 == 0,
       # 'segundo_redondo': segundos%10 == 0,
       # 'listado_de_numeros': list(range(25))
    #}
 #   
#
    #contexto = Context(diccionario)
    #
    #renderizar_template = template.render(contexto)
    #
    #return HttpResponse(renderizar_template)
    
    
    #V3
    
#def inicio(resquest):
    
   # template = loader.get_template('inicio.html')
    
    #segundos = datetime.now().second
   # diccionario = {
    #    'mensaje': 'Este es el mensaje de inicio...',
    #    'segundos': segundos,
   #     'segundo_par': segundos%2 == 0,
  #      'segundo_redondo': segundos%10 == 0,
  #      'listado_de_numeros': list(range(25))
   #}
    
   # contexto = Context(diccionario)
    #renderizar_template = template.render(contexto)
  #  renderizar_template = template.render(diccionario)
 #   return HttpResponse(renderizar_template)


#def segunda_vista(request):
 #   return HttpResponse('<h1>Soy la segunda vista</h1>')

#def fecha_actual(request):
  #  fecha = datetime.now()
 #   return HttpResponse(f'<h1>Fecha actual: {fecha}</h1>')

#def saludar(request):
 #   return HttpResponse('Bienvenido/a!!!')

#def bienvenida(request, nombre, apellido):
  #  return HttpResponse(f'Bienvenido/a {nombre.title()} {apellido.title()}!!!')

#def crear_perro(request, nombre, edad):
   # template = loader.get_template('crear_perro.html')
   # perro = Perro(nombre=nombre, edad=edad)
   # perro.save()
   # diccionario = {
   #    'perro': perro,
   # }
    
   # renderizar_template = template.render(diccionario)
  #  return HttpResponse(renderizar_template)





#v4
@login_required
def prueba(request):
    
   # template = loader.get_template('inicio.html')
    
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'segundo_redondo': segundos%10 == 0,
        'listado_de_numeros': list(range(25))
    }
    
   # contexto = Context(diccionario)
    #renderizar_template = template.render(contexto)
   # renderizar_template = template.render(diccionario)
    #return HttpResponse(renderizar_template)
    return render(request, 'inicio/prueba.html', diccionario)


def inicio(request):
  return render(request, 'inicio/inicio.html')

def segunda_vista(request):
    return HttpResponse('<h1>Soy la segunda vista</h1>')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Fecha actual: {fecha}</h1>')

def saludar(request):
    return HttpResponse('Bienvenido/a!!!')

def bienvenida(request, nombre, apellido):
    return HttpResponse(f'Bienvenido/a {nombre.title()} {apellido.title()}!!!')

#v1
#def crear_perro(request, nombre, edad):
 #   template = loader.get_template('crear_perro.html')
  #  perro = Perro(nombre=nombre, edad=edad)
  #  perro.save()
   # diccionario = {
   #    'perro': perro,
   # }
    #
   # renderizar_template = template.render(diccionario)
    #return HttpResponse(renderizar_template)
  
  #v2  
#def crear_perro(request, nombre, edad):
 #   perro = Perro(nombre=nombre, edad=edad)
  #  perro.save()
  #  diccionario = {
  #     'perro': perro,
  #  }
  #  
  #  return render(request, 'inicio/crear_perro.html', diccionario)
  
  #v3 
  
#def crear_perro(request):
 #   print('================================')
  #  print('================================')
  #  print(request.POST)
  #  print('================================')
  #  print('================================')
  #  print(request.GET)
 #   print('================================')
 #   print('================================')
    
 #   diccionario = {}
    
 #   if request.method == "POST":
 #       perro = Perro(nombre=request.POST['nombre'], edad=request.POST['edad'])
 #       perro.save()
 #       diccionario['perro'] = perro
        
 #   return render(request, 'inicio/crear_perro.html', diccionario) 


#v4  
#def crear_perro(request):
 #   
  #  if request.method == "POST":
   #     formulario = CrearPerroFormulario(request.POST)
   #     if formulario.is_valid():
   #         info = formulario.cleaned_data
   #         perro = Perro(nombre=info['nombre'], edad=info['edad'])
   #         perro.save()
   #         return redirect('inicio:listar_perros')               
   #     else:
   #         return render(request, 'inicio/crear_perro.html', {'formulario': formulario})               
    
    #formulario = CrearPerroFormulario()
   # return render(request, 'inicio/crear_perro.html', {'formulario': formulario})
  
def listar_perros(request):
    formulario = BuscarPerroFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_de_perros = Perro.objects.filter(nombre__icontains=nombre_a_buscar)
        
    formulario = BuscarPerroFormulario()        
    return render(request, 'inicio/listar_perros.html', {'formulario': formulario, 'perros': listado_de_perros})
  
def eliminar_perro(request, perro_id):
    
    perro = Perro.objects.get(id=perro_id)
    perro.delete()
    
    return redirect('inicio:listar_perros')

def modificar_perro(request, perro_id):
    perro_a_modificar = Perro.objects.get(id=perro_id)               
  
    if request.method == 'POST':
        formulario = ModificarPerroFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            perro_a_modificar.nombre = info['nombre']
            perro_a_modificar.edad = info['edad']
            perro_a_modificar.save()
            return redirect('inicio:listar_perros')
        else:
            return render(request, 'inicio/modificar_perro.html', {'formulario': formulario})
    
    formulario = ModificarPerroFormulario(initial={'nombre': perro_a_modificar.nombre, 'edad': perro_a_modificar.edad})
    return render(request, 'inicio/modificar_perro.html', {'formulario': formulario})


class CrearPerro(CreateView):
    model = Perro
    template_name = 'inicio/CBV/crear_perro_CBV.html'
    fields = ['nombre', 'edad', 'descripcion']
    success_url = reverse_lazy('inicio:listar_perros')
    
class ListarPerros(ListView):
    model = Perro
    template_name = "inicio/CBV/listar_perros_CBV.html"
    context_object_name = 'perros'
    
    def get_queryset(self):
        listado_de_perros = []
        formulario = BuscarPerroFormulario(self.request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data['nombre']
            listado_de_perros = Perro.objects.filter(nombre__icontains=nombre_a_buscar)
        return listado_de_perros
    
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)   
        contexto['formulario'] = BuscarPerroFormulario()
        return contexto
    
    
class ModificarPerro(LoginRequiredMixin, UpdateView):
    model = Perro
    template_name = "inicio/CBV/modificar_perro_CBV.html"
    fields = ['nombre', 'edad', 'descripcion']
    success_url = reverse_lazy('inicio:listar_perros')
      
class EliminarPerro(LoginRequiredMixin, DeleteView):
    model = Perro
    template_name = "inicio/CBV/eliminar_perro_CBV.html"
    success_url = reverse_lazy('inicio:listar_perros')

class MostrarPerro(DetailView):
    model = Perro
    template_name = "inicio/CBV/mostrar_perro_CBV.html"

