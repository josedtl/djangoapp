from django.db import models


class CargoModel(models.Model):
    CargoId = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    FechaRegistro = models.DateTimeField(auto_now_add=True)
    CodUsuario = models.CharField(max_length=15)
    EstadoRegistro = models.BooleanField(default=True)

    class Meta:
        db_table = "catalogo_cargo"  # Personaliza el nombre de la tabla
