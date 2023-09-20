from rest_framework import serializers
from .models import Alumno, Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    detalles = CursoSerializer(many=True, read_only=True)

    class Meta:
        model = Alumno
        fields = '__all__'