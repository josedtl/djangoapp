from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PersonaNaturalViewSet,
    CatalogoPersonaNaturalViewSet,
    CatalogoPersonaNaturalMedioComunicacionViewSet,
    EstadoCivilViewSet,
    GeneroViewSet,
    UbigeoViewSet,
    TipoDocumentoIdentidadViewSet,
)

router = DefaultRouter()
router.register(r"personas", PersonaNaturalViewSet)
router.register(r"catalogo_personanatural", CatalogoPersonaNaturalViewSet)
router.register(
    r"catalogo_personanaturalmediocomunicacion",
    CatalogoPersonaNaturalMedioComunicacionViewSet,
)
router.register(r"EstadoCivil", EstadoCivilViewSet)
router.register(r"Genero", GeneroViewSet)
router.register(r"Ubigeo", UbigeoViewSet)
router.register(r"TipoDocumentoIdentidad", TipoDocumentoIdentidadViewSet)

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("", include(router.urls)),
    path("docs/", include_docs_urls(title="Tasks API")),
]
