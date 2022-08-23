from rest_framework import serializers
from .models import Person

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['data']