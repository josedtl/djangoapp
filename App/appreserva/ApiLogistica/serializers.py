from rest_framework import serializers
from .models import Pedido, Producto, DetallePedido,Cabecera, Detalle

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = DetallePedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'


class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle
        fields = '__all__'

class CabeceraSerializer(serializers.ModelSerializer):
    detalles = DetalleSerializer(many=True, read_only=True)

    class Meta:
        model = Cabecera
        fields = '__all__'