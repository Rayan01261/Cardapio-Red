from django.contrib import admin
from .models import Pedido, Comanda

@admin.register(Comanda)
class ComandaAdmin(admin.ModelAdmin):
    list_display = ['total', 'sub_total', 'data_criacao']
    search_fields = ['Pedido']
    
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['item','quantidade']
    search_fields = ['item']
