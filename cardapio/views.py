from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Mesa, Item, Categoria, Cardapio
from .serializers import MesaSerializer, ItemSerializer, CategoriaSerializer, CardapioSerializer

class MesaViewSet(ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class CardapioViewSet(ModelViewSet):
    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
