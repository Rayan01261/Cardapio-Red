from django.db import models
from cardapio.models import Mesa, Item

class Comanda(models.Model):  
    
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    data_criacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        # db_table = "Comanda"
        ordering = ["data_criacao"]
        verbose_name = 'Comanda'
        verbose_name_plural = 'Comandas'
   
class Pedido(models.Model):
    
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, related_name='pedidos')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        # db_table = "Pedido"
        ordering = ["data_criacao"]
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    