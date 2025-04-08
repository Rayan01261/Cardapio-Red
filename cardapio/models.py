from django.db import models

class Item(models.Model):
    valor = models.DecimalField(decimal_places=2)
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)

class Cardapio(models.Model):
    itens = models.ManyToManyField(Item)

class Mesa(models.Model):
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE)

class Comanda(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)