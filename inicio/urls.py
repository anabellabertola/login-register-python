from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('prueba/', views.prueba, name='prueba'),
    path('segunda-vista/', views.segunda_vista, name='segunda-vista'),
    path('fecha-actual/', views.fecha_actual, name='fecha-actual'),
    path('saludar/', views.saludar, name='saludar'),
    path('bienvenida/<str:nombre>/<str:apellido>', views.bienvenida, name='bienvenida'),  
   
   # VISTAS COMUNES
   
    #v1 crear perro
    #path('crear-perro/<str:nombre>/<int:edad>', views.crear_perro, name='crear-perro'), 
    #v2
    #path('perros/', views.listar_perros, name='listar_perros'),
   # path('perros/crear/', views.crear_perro, name='crear_perro'),
   # path('perros/eliminar/<int:perro_id>', views.eliminar_perro, name='eliminar_perro'),
   # path('perros/modificar/<int:perro_id>', views.modificar_perro, name='modificar_perro'),

    #CBV 
    path('perros/', views.ListarPerros.as_view(), name='listar_perros'),
    path('perros/crear/', views.CrearPerro.as_view(), name='crear_perro'),
    path('perros/eliminar/<int:pk>/', views.EliminarPerro.as_view(), name='eliminar_perro'),
    path('perros/modificar/<int:pk>/', views.ModificarPerro.as_view(), name='modificar_perro'),
    path('perros/<int:pk>/', views.MostrarPerro.as_view(), name='mostrar_perro'),
]