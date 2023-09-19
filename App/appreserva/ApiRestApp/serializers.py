from rest_framework import serializers
from .models import (
    PersonaNatural,
    CatalogoPersonaNatural,
    CatalogoPersonaNaturalMedioComunicacion,
    TipoDocumentoIdentidad,
    Genero,
    EstadoCivil,
    Ubigeo,
)


class TipoDocumentoIdentidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoIdentidad
        fields = "__all__"


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"


class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = "__all__"


class UbigeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubigeo
        fields = "__all__"


class PersonaNaturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaNatural
        fields = "__all__"


class CatalogoPersonaNaturalMedioComunicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoPersonaNaturalMedioComunicacion
        fields = "__all__"


class CatalogoPersonaNaturalSerializer(serializers.ModelSerializer):
    detalles = CatalogoPersonaNaturalMedioComunicacionSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = CatalogoPersonaNatural
        fields = [
            "id",
            "NumDocumento",
            "Nombres",
            "ApellidoPaterno",
            "ApellidoMaterno",
            "FechaNacimiento",
            "Direccion",
            "Telefono",
            "Correo",
            "FechaRegistro",
            "CodUsuario",
            "EstadoRegistro",
            "TipoDocumentoIdentidadId",
            "UbigeoId",
            "GeneroId",
            "EstadoCivilId",
            "detalles",
        ]

    def create(self, validated_data):
        detalles_data = validated_data.pop("detalles")
        cabecera = CatalogoPersonaNatural.objects.create(**validated_data)
        for detalle_data in detalles_data:
            CatalogoPersonaNaturalMedioComunicacion.objects.create(
                cabecera=cabecera, **detalle_data
            )
        return cabecera
