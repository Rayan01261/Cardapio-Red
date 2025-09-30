from django.db import models
from cardapio.models import Mesa, Item

class Comanda(models.Model):  
    
    total = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    data_criacao = models.DateTimeField(auto_now=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)

    def atualizar_total(self):
        total = 0
        for pedido in self.pedidos.all():
            if pedido.item:  
                total += pedido.item.preço * pedido.quantidade
        self.total = total
        self.sub_total = total  # se for a mesma lógica
        self.save(update_fields=["total", "sub_total"])

    class Meta:
        # db_table = "Comanda"
        ordering = ["data_criacao"]
        verbose_name = 'Comanda'
        verbose_name_plural = 'Comandas'


class Pedido(models.Model):
    item = models.ForeignKey(Item,null=True, on_delete=models.SET_NULL)
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, related_name="pedidos")
    quantidade = models.IntegerField(default=1)
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.comanda.atualizar_total()

    def delete(self, *args, **kwargs):
        comanda = self.comanda
        super().delete(*args, **kwargs)
        comanda.atualizar_total()

    class Meta:
        # db_table = "Pedido"
        ordering = []
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    