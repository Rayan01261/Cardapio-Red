from rest_framework import serializers
from .models import Item, Cardapio, Mesa, Categoria

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = '__all__'
        
class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = '__all__'

class CardapioSerializer(serializers.ModelSerializer):
    itens = ItemSerializer(many=True)

    class Meta:
        model = Cardapio
        fields = '__all__'


class MesaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mesa
        fields = '__all__'


