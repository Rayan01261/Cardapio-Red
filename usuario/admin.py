from django.contrib import admin
from .models import Garcom, Gerente

@admin.register(Gerente)
class GerenteAdmin(admin.ModelAdmin):
    list_display = ['mome_completo', 'idade', 'cpf', 'data_nascimento', 'telefone', 'data_criacao', 'ativo']
    search_fields = ['cpf']
    
@admin.register(Garcom)
class GarcomAdmin(admin.ModelAdmin):
    list_display = ['mome_completo', 'idade', 'cpf', 'data_nascimento', 'telefone', 'data_criacao', 'avaliacao_estrelas', 'qtd_vendas']
    search_fields = ['cpf']

