from django.contrib import admin
from .models import Pedido, Comanda

@admin.register(Comanda)
class ComandaAdmin(admin.ModelAdmin):
    list_display = ['mesa', 'total', 'sub_total', 'data_criacao']
    search_fields = ['mesa']
    
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['comanda', 'item', 'quantidade', 'data_criacao']
    search_fields = ['comanda']
