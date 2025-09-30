from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Comanda, Pedido
from .serializers import ComandaSerializer, PedidoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ComandaViewSet(ModelViewSet):
    
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['mesa']


class PedidoViewSet(ModelViewSet):
    
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
