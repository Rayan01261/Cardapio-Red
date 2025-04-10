from rest_framework import serializers
from .models import Item, Cardapio, Mesa, Comanda

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CardapioSerializer(serializers.ModelSerializer):
    itens = ItemSerializer(many=True)

    class Meta:
        model = Cardapio
        fields = '__all__'

class MesaSerializer(serializers.ModelSerializer):
    cardapio = CardapioSerializer()

    class Meta:
        model = Mesa
        fields = '__all__'

class ComandaSerializer(serializers.ModelSerializer):
    mesa = MesaSerializer()

    class Meta:
        model = Comanda
        fields = '__all__'
