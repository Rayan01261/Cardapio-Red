from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Comanda, Pedido
from .serializers import ComandaSerializer, PedidoSerializer

class ComandaViewSet(ModelViewSet):
    
    queryset = Comanda.objects.all()
    serializer_clas = ComandaSerializer


class PedidoViewSet(ModelViewSet):
    
    queryset = Pedido.objects.all()
    serializer_clas = PedidoSerializer
