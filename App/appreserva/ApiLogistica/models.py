from django.db import models

class Pedido(models.Model):
    fecha_pedido = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)


class Cabecera(models.Model):
    # Campos de tu cabecera
    nombre = models.CharField(max_length=100)
    # Otros campos
    
class Detalle(models.Model):
    cabecera = models.ForeignKey(Cabecera, on_delete=models.CASCADE)
    # Campos de tu detalle
    nombre = models.CharField(max_length=100)
    # Otros campos

# Define el enumerado para los estados
class Estado(models.IntegerChoices):
    LOAD = 0, 'load'
    ADD = 1, 'add'
    DELETE = 2, 'delete'
    UPDATE = 3, 'update'