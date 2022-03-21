from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from sepulkas.models import Sepulka
from sepulkas.api.serializer import SepulkaSerializer

class SepulckaViewSet(ModelViewSet):
    queryset = Sepulka.objects.all()
    serializer_class = SepulkaSerializer

    permission_classes = [permissions.IsAuthenticated]

