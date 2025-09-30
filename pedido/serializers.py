from rest_framework import serializers
from .models import Pedido, Comanda, Item
from cardapio.serializers import ItemSerializer

class PedidoSerializer(serializers.ModelSerializer):

    item = ItemSerializer(read_only=True)  # mostra dados do item
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(), source="item", write_only=True
    )

    class Meta:
        model = Pedido
        fields = '__all__'

class ComandaSerializer(serializers.ModelSerializer):
    pedidos = PedidoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Comanda
        fields = '__all__'

