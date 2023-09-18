from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonaNaturalViewSet

router = DefaultRouter()
router.register(r"personas", PersonaNaturalViewSet)
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("", include(router.urls)),
    path("docs/", include_docs_urls(title="Tasks API")),
]
