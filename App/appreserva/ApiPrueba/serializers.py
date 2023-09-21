from rest_framework import serializers
from .models import Alumno, Curso
from .modelsItem.CargoModel import CargoModel
from .modelsItem.PersonaNaturalModel import PersonaNaturalModel
from .modelsItem.GeneralModel import TipoDocumentoIdentidad, EstadoCivil, Genero, Ubigeo


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class AlumnoSerializer(serializers.ModelSerializer):
    detalles = CursoSerializer(many=True, read_only=True)

    class Meta:
        model = Alumno
        fields = "__all__"


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoModel
        fields = "__all__"


class PersonaNaturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaNaturalModel
        fields = "__all__"


class TipoDocumentoIdentidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumentoIdentidad
        fields = "__all__"


class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = "__all__"


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"


class UbigeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubigeo
        fields = "__all__"


from .models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    NomTipoDocumento = serializers.SerializerMethodField()
    NomTipoDocumentoAll = serializers.SerializerMethodField()

    class Meta:
        model = Persona
        fields = [
            "PersonaId",
            "NomTipoDocumento",
            "NomTipoDocumentoAll",
            "Nombres",
            "Apellidos",
        ]

    def get_NomTipoDocumento(self, obj):
        return obj.TipodocumentoId.Descripcion

    def get_NomTipoDocumentoAll(self, obj):
        return obj.TipodocumentoId.Descripcion


class PersonaNaturalMainSerializer(serializers.ModelSerializer):
    NomDocumento = serializers.SerializerMethodField()

    # NomUbigeo = serializers.SerializerMethodField()
    class Meta:
        model = PersonaNaturalModel
        fields = [
            "PersonaNaturalId",
            "NomDocumento",
            "NumDocumento",
            "Nombres",
            "ApellidoPaterno",
            "ApellidoMaterno",
            "FechaRegistro",
            "CodUsuario",
        ]

    def get_NomDocumento(self, obj):
        return obj.TipoDocumentoIdentidad.Alias


    # def get_NomUbigeo(self, obj):
    #     return obj.UbigeoId.Nombre
