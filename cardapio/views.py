from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Comanda
from .serializers import ComandaSerializer

class ComandaViewSet(ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer
