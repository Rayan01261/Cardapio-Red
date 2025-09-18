from rest_framework import serializers
from .models import Pedido, Comanda


class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'