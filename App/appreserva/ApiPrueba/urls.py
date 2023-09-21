from django.urls import path, include
from .views import GuardarAlumnoYCurso
from rest_framework.documentation import include_docs_urls
from .views import (
    CargoListCreateView,
    CargoDetailView,
    CargoSave,
    TipoDocumentoIdentidadViewSet,
    UbigeoViewSet,
    EstadoCivilViewSet,
    GeneroViewSet,
    PersonaNaturalViewSet,
)
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"PersonaNatural", PersonaNaturalViewSet)
router.register(r"TipoDocumentoIdentidad", TipoDocumentoIdentidadViewSet)
router.register(r"Ubigeo", UbigeoViewSet)
router.register(r"EstadoCivil", EstadoCivilViewSet)
router.register(r"Genero", GeneroViewSet)
urlpatterns = [
    path("cargos/", CargoListCreateView.as_view(), name="cargo-list-create"),
    path("cargos/<int:pk>/", CargoDetailView.as_view(), name="cargo-detail"),
    path(
        "guardar-alumno-y-curso/",
        GuardarAlumnoYCurso.as_view(),
        name="guardar_alumno_y_curso",
    ),
    path(
        "cargos/SaveItem/",
        CargoSave.as_view(),
        name="cargos",
    ),
    path("docs/", include_docs_urls(title="Documento")),
    path("", include(router.urls)),
    path("personas/", views.PersonaListView.as_view(), name="persona-list"),
    path("personasMain/", views.PersonaNaturalMainListView.as_view(), name="main"),
]
