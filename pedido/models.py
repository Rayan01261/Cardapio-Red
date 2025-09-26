from django.db import models
from cardapio.models import Mesa, Item

class Pedido(models.Model):
    item = models.ForeignKey(Item,null=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=1)
    
    class Meta:
        # db_table = "Pedido"
        ordering = []
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'


class Comanda(models.Model):  
    
    pedido = models.ManyToManyField(Pedido)
    total = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    data_criacao = models.DateTimeField(auto_now=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)

    class Meta:
        # db_table = "Comanda"
        ordering = ["data_criacao"]
        verbose_name = 'Comanda'
        verbose_name_plural = 'Comandas'



    