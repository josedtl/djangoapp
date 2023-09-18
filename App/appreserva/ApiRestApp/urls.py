from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonaNaturalViewSet

router = DefaultRouter()
router.register(r'personas', PersonaNaturalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
