from django.contrib import admin
from .models import Garcom, Gerente

@admin.register(Gerente)
class GerenteAdmin(admin.ModelAdmin):
    # list_display = ['nome_completo', 'idade', 'cpf', 'data_nascimento', 'telefone', 'data_criacao', 'ativo']
    list_display = ['nome_completo', 'idade', 'cpf', 'data_nascimento', 'telefone', 'data_criacao']
    search_fields = ['cpf']
    
@admin.register(Garcom)
class GarcomAdmin(admin.ModelAdmin):
    # list_display = ['nome_completo', 'idade', 'cpf', 'data_nascimento', 'telefone', 'data_criacao', 'avaliacao_estrelas', 'qtd_vendas']
    list_display = ['nome_completo', 'idade', 'cpf', 'data_nascimento', 'telefone', 'data_criacao', 'qtd_vendas']
    search_fields = ['cpf']

