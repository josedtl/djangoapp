from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Estado, Pedido, Producto, DetallePedido, Cabecera, Detalle
from .serializers import (
    PedidoSerializer,
    ProductoSerializer,
    DetallePedidoSerializer,
    CabeceraSerializer,
    DetalleSerializer,
)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer



class CabeceraDetalleView(APIView):
    def post(self, request, format=None):
        data = request.data
        
        cabecera_estado = data.get('cabecera_estado')
        detalle_estado = data.get('detalle_estado')
        
        # Crear la cabecera
        cabecera_serializer = CabeceraSerializer(data={'fecha': data.get('fecha')})
        if cabecera_serializer.is_valid():
            cabecera_serializer.save()
            cabecera = cabecera_serializer.instance
        else:
            return Response(cabecera_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if cabecera_estado == Estado.ADD:
            # Código para guardar el detalle
            detalle_serializer = DetalleSerializer(data={'cabecera': cabecera.id, 'producto': data.get('producto'), 'cantidad': data.get('cantidad')})
            if detalle_serializer.is_valid():
                detalle_serializer.save()
            else:
                cabecera.delete()
                return Response(detalle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif cabecera_estado == Estado.UPDATE:
            # Código para actualizar el detalle
            detalle_id = data.get('detalle_id')
            try:
                detalle = Detalle.objects.get(pk=detalle_id, cabecera=cabecera)
                detalle_serializer = DetalleSerializer(detalle, data={'producto': data.get('producto'), 'cantidad': data.get('cantidad')}, partial=True)
                if detalle_serializer.is_valid():
                    detalle_serializer.save()
                else:
                    return Response(detalle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Detalle.DoesNotExist:
                cabecera.delete()
                return Response({'error': 'El detalle especificado no existe en esta cabecera.'}, status=status.HTTP_400_BAD_REQUEST)
        elif cabecera_estado == Estado.DELETE:
            # Código para eliminar el detalle
            detalle_id = data.get('detalle_id')
            try:
                detalle = Detalle.objects.get(pk=detalle_id, cabecera=cabecera)
                detalle.delete()
            except Detalle.DoesNotExist:
                cabecera.delete()
                return Response({'error': 'El detalle especificado no existe en esta cabecera.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Cabecera y detalle guardados con éxito.'}, status=status.HTTP_201_CREATED)