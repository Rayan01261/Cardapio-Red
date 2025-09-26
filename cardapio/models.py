from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class Categoria(models.Model):
    
    nome_categoria = models.CharField(max_length=50)
    
    class Meta:
        # db_table = "Categoria"
        # ordering = [""]
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Item(models.Model):
    
    preço = models.DecimalField(decimal_places=2, max_digits=5)
    nome = models.CharField(max_length=20)
    # colocar pro BD ser NULL
    descricao = models.CharField(blank=True, max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="itens")
    class Meta:
        # db_table = "Item"
        # ordering = [""]
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
    


       
        
class Cardapio(models.Model):
    Categoria = models.ManyToManyField(Categoria)
    
    class Meta:
        # db_table = "Cardapio"
        # ordering = [""]
        verbose_name = 'Cardapio'
        verbose_name_plural = 'Cardapios'


class Mesa(models.Model):
    ocupada = models.BooleanField(default=False)
    class Meta:
        # db_table = "Mesa"
        # ordering = [""]
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'