from django.db import models

class Alumno(models.Model):
    AlumnoId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'Catalogo_Alumno'  # Personaliza el nombre de la tabla
class Curso(models.Model):
    CursoId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    # AlumnoId = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    AlumnoId = models.ForeignKey(Alumno, on_delete=models.CASCADE, db_column='AlumnoId')

    class Meta:
        db_table = 'Catalogo_Curso'  # Personaliza el nombre de la tabla
from enum import Enum

class Accion(Enum):
    LOAD = 0
    ADD = 1
    DELETE = 2
    UPDATE = 3


class TipoDocumento(models.Model):
    TipodocumentoId = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.Descripcion

class Persona(models.Model):
    PersonaId = models.AutoField(primary_key=True)
    TipodocumentoId = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    Nombres = models.CharField(max_length=255)
    Apellidos = models.CharField(max_length=255)

    def __str__(self):
        return self.Nombres