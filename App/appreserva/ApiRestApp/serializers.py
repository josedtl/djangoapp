from rest_framework import serializers
from .models import PersonaNatural

class PersonaNaturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaNatural
        fields = '__all__'
