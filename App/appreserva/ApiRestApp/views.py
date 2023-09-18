from rest_framework import viewsets
from .models import PersonaNatural
from .serializers import PersonaNaturalSerializer

class PersonaNaturalViewSet(viewsets.ModelViewSet):
    queryset = PersonaNatural.objects.all()
    serializer_class = PersonaNaturalSerializer
