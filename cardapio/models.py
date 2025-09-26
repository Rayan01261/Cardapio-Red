from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class Item(models.Model):
    
    preço = models.DecimalField(decimal_places=2, max_digits=5)
    nome = models.CharField(max_length=20)
    # colocar pro BD ser NULL
    descricao = models.CharField(blank=True, max_length=100)

    class Meta:
        # db_table = "Item"
        # ordering = [""]
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
    

class Categoria(models.Model):
    
    nome_categoria = models.CharField(max_length=50)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    class Meta:
        # db_table = "Categoria"
        # ordering = [""]
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
       
        
class Cardapio(models.Model):
    Categoria = models.ManyToManyField(Categoria)
    
    class Meta:
        # db_table = "Cardapio"
        # ordering = [""]
        verbose_name = 'Cardapio'
        verbose_name_plural = 'Cardapios'


class Mesa(models.Model):
    
    class Meta:
        # db_table = "Mesa"
        # ordering = [""]
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'