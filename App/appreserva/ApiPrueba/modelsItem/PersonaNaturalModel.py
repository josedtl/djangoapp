from django.db import models
from .GeneralModel import TipoDocumentoIdentidad, Ubigeo, Genero, EstadoCivil


class PersonaNaturalModel(models.Model):
    PersonaNaturalId = models.AutoField(primary_key=True)
    TipoDocumentoIdentidad = models.ForeignKey(
        TipoDocumentoIdentidad,
        on_delete=models.CASCADE,
        db_column="TipoDocumentoIdentidadId",
    )
    NumDocumento = models.CharField(max_length=255, default="")
    Nombres = models.CharField(max_length=255, default="")
    ApellidoPaterno = models.CharField(max_length=255, default="")
    ApellidoMaterno = models.CharField(max_length=255, default="")
    FechaNacimiento = models.DateField(default=None)
    UbigeoId = models.ForeignKey(
        Ubigeo,
        on_delete=models.CASCADE,
        db_column="UbigeoId",
    )
    Direccion = models.CharField(max_length=255, default="")
    Telefono = models.CharField(max_length=255, default="")
    Correo = models.EmailField(max_length=255, default="")
    GeneroId = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        db_column="GeneroId",
    )
    EstadoCivilId = models.ForeignKey(
        EstadoCivil,
        on_delete=models.CASCADE,
        db_column="EstadoCivilId",
    )
    FechaRegistro = models.DateTimeField(default=None)
    CodUsuario = models.CharField(max_length=255, default="")
    EstadoRegistro = models.BooleanField(default=True)

    class Meta:
        db_table = "Catalogo_PersonaNatural"  # Personaliza el nombre de la tabla
