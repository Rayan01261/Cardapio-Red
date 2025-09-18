from .models import Gerente, Garcom
from .serializers import GerenteSerializer, GarcomSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class GerenteViewSet(ModelViewSet):
    queryset = Gerente.objects.all()
    serializer_class = GerenteSerializer
    
    
class GarcomViewSet(ModelViewSet):
    queryset = Garcom.objects.all()
    serializer_class = GarcomSerializer
    
    