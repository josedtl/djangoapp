from django.db import models


class TipoDocumentoIdentidad(models.Model):
    TipoDocumentoIdentidadId = models.AutoField(primary_key=True)
    Codigo = models.CharField(max_length=30)
    Alias = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=150)
    EsEmpresa = models.BooleanField(default=True)

    class Meta:
        db_table = (
            "Catalogo_TipoDocumentoIdentidad"  # Personaliza el nombre de la tabla
        )


class Ubigeo(models.Model):
    UbigeoId = models.AutoField(primary_key=True)
    Codigo = models.CharField(max_length=6, unique=True)
    Nombre = models.CharField(max_length=255)

    class Meta:
        db_table = (
            "Catalogo_Ubigeo"  # Personaliza el nombre de la tabla
        )


class Genero(models.Model):
    GeneroId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)

    class Meta:
        db_table = (
            "Catalogo_Genero"  # Personaliza el nombre de la tabla
        )


class EstadoCivil(models.Model):
    EstadoCivilId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)

    class Meta:
        db_table = (
            "Catalogo_EstadoCivil"  # Personaliza el nombre de la tabla
        )
