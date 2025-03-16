from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/crear/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),
    path('registro/', views.registro, name='registro'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('', views.inicio, name='inicio'),    
    path('principal/', views.principal, name='principal'),
    path('historias-medicas/crear/', views.crear_historia_medica, name='crear_historia_medica'),
    path('historias-medicas/<int:historia_id>/anamnesis/crear/', views.crear_anamnesis, name='crear_anamnesis'),
    path('historias-medicas/', views.lista_historias_medicas, name='lista_historias_medicas'),
    path('historias-medicas/<int:historia_id>/editar/', views.editar_historia_medica, name='editar_historia_medica'),
    path('historias-medicas/<int:historia_id>/eliminar/', views.eliminar_historia_medica, name='eliminar_historia_medica'),
    path('anamnesis/<int:anamnesis_id>/completar/', views.completar_anamnesis, name='completar_anamnesis'),
    path('crear-representante/', views.crear_representante, name='crear_representante'),

]
