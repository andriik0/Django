from rest_framework import serializers
from sepulkas.models import Sepulka


class SepulkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sepulka
        fields = [
            'id',
            'coefficient',
            'slug',
        ]
    