from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PedidoViewSet,ProductoViewSet,CabeceraDetalleView
)
from rest_framework.documentation import include_docs_urls
router = DefaultRouter()
router.register(r"Pedido", PedidoViewSet)
router.register(r"Producto", ProductoViewSet)
# router.register(r"Cabecera", CabeceraDetalleView)
urlpatterns = [
    path("", include(router.urls)),
    path("docs/", include_docs_urls(title="Tasks API")),
     path('cabecera-detalle/', CabeceraDetalleView.as_view(), name='cabecera-detalle'),
]