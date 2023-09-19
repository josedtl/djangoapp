from django.db import models

class PersonaNatural(models.Model):
    PersonaNaturalId = models.AutoField(primary_key=True)
    NumDocumento = models.CharField(max_length=20)
    Nombres = models.CharField(max_length=100)
    ApellidoPaterno = models.CharField(max_length=100)
    ApellidoMaterno = models.CharField(max_length=100)
    FechaNacimiento = models.DateField()
    Direccion = models.CharField(max_length=200)
    Correo = models.EmailField()
    Telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.Nombres



class TipoDocumentoIdentidad(models.Model):
    # Define los campos para TipoDocumentoIdentidad
    nombre = models.CharField(max_length=255)

class Genero(models.Model):
    # Define los campos para Genero
    nombre = models.CharField(max_length=255)

class EstadoCivil(models.Model):
    # Define los campos para EstadoCivil
    nombre = models.CharField(max_length=255)

class Ubigeo(models.Model):
    # Define los campos para Ubigeo
    nombre = models.CharField(max_length=255)

class CatalogoPersonaNatural(models.Model):
    # Define los campos para CatalogoPersonaNatural
    TipoDocumentoIdentidadId = models.ForeignKey(TipoDocumentoIdentidad, on_delete=models.SET_NULL, null=True)
    NumDocumento = models.CharField(max_length=255, null=True)
    Nombres = models.CharField(max_length=50)
    ApellidoPaterno = models.CharField(max_length=50)
    ApellidoMaterno = models.CharField(max_length=50)
    FechaNacimiento = models.DateTimeField(null=True)
    UbigeoId = models.ForeignKey(Ubigeo, on_delete=models.SET_NULL, null=True)
    Direccion = models.CharField(max_length=100, null=True)
    Telefono = models.CharField(max_length=15, null=True)
    Correo = models.EmailField(max_length=50, null=True)
    GeneroId = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    EstadoCivilId = models.ForeignKey(EstadoCivil, on_delete=models.SET_NULL, null=True)
    FechaRegistro = models.DateTimeField(null=True)
    CodUsuario = models.CharField(max_length=25, null=True)
    EstadoRegistro = models.BooleanField(null=True)

class CatalogoPersonaNaturalMedioComunicacion(models.Model):
    # Define los campos para CatalogoPersonaNaturalMedioComunicacion
    PersonaNaturalId = models.ForeignKey(CatalogoPersonaNatural, on_delete=models.CASCADE)
    MedioComunicacionId = models.IntegerField(null=True)
    Dato = models.CharField(max_length=100, null=True)
    FechaRegistro = models.DateTimeField(null=True)
    CodUsuario = models.CharField(max_length=25, null=True)
    EstadoRegistro = models.BooleanField(null=True)