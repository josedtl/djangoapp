from rest_framework import viewsets
from .models import (
    PersonaNatural,
    CatalogoPersonaNatural,
    CatalogoPersonaNaturalMedioComunicacion,
    TipoDocumentoIdentidad,
    Genero,
    EstadoCivil,
    Ubigeo,
)
from .serializers import (
    PersonaNaturalSerializer,
    CatalogoPersonaNaturalSerializer,
    CatalogoPersonaNaturalMedioComunicacionSerializer,
    EstadoCivilSerializer,
    TipoDocumentoIdentidadSerializer,
    GeneroSerializer,
    UbigeoSerializer,
)


class EstadoCivilViewSet(viewsets.ModelViewSet):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer


class TipoDocumentoIdentidadViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumentoIdentidad.objects.all()
    serializer_class = TipoDocumentoIdentidadSerializer


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class UbigeoViewSet(viewsets.ModelViewSet):
    queryset = Ubigeo.objects.all()
    serializer_class = UbigeoSerializer


class PersonaNaturalViewSet(viewsets.ModelViewSet):
    queryset = PersonaNatural.objects.all()
    serializer_class = PersonaNaturalSerializer


class CatalogoPersonaNaturalViewSet(viewsets.ModelViewSet):
    queryset = CatalogoPersonaNatural.objects.all()
    serializer_class = CatalogoPersonaNaturalSerializer


class CatalogoPersonaNaturalMedioComunicacionViewSet(viewsets.ModelViewSet):
    queryset = CatalogoPersonaNaturalMedioComunicacion.objects.all()
    serializer_class = CatalogoPersonaNaturalMedioComunicacionSerializer
