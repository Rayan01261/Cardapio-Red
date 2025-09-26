from django.contrib import admin
from .models import Item, Categoria, Cardapio, Mesa


class ItemInline(admin.TabularInline):  # permite editar itens dentro da categoria
    model = Item
    extra = 1  # quantas linhas extras aparecem


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria')
    search_fields = ('nome_categoria',)
    inlines = [ItemInline]  # mostra os itens dentro da categoria


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preço', 'descricao', 'categoria')
    search_fields = ('nome',)
    list_filter = ('categoria',)


@admin.register(Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display = ('id',)
    filter_horizontal = ('Categoria',)  # facilita escolher várias categorias


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ocupada')
    list_filter = ('ocupada',)
