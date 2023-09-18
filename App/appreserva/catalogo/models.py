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
    Telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.Nombres
