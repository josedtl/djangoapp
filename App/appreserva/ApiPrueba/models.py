from django.db import models

class Alumno(models.Model):
    AlumnoId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)

class Curso(models.Model):
    CursoId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    # AlumnoId = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    AlumnoId = models.ForeignKey(Alumno, on_delete=models.CASCADE, db_column='AlumnoId')

from enum import Enum

class Accion(Enum):
    LOAD = 0
    ADD = 1
    DELETE = 2
    UPDATE = 3
