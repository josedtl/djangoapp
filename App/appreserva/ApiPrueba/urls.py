from django.urls import path
from .views import GuardarAlumnoYCurso
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('guardar-alumno-y-curso/', GuardarAlumnoYCurso.as_view(), name='guardar_alumno_y_curso'),
            path("docs/", include_docs_urls(title="Documento")),
]