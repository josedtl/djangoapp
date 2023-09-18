from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_personas_naturales, name='listar_personas_naturales'),
    path('crear/', views.crear_persona_natural, name='crear_persona_natural'),
    path('editar/<int:persona_id>/', views.editar_persona_natural, name='editar_persona_natural'),
    path('eliminar/<int:persona_id>/', views.eliminar_persona_natural, name='eliminar_persona_natural'),
]
