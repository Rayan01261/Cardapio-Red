from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


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

class Pessoa(AbstractUser):
    
    idade = models.IntegerField()
    cpf = models.CharField(max_length=15, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="O número deve estar no formato: '+5511999998888'. Máximo de 15 dígitos."
        )
    ])  
    
class Administrador_sistema(Pessoa):
    ativo = models.BooleanField(default=False)

class Garçom(Pessoa):  
     
    avaliacao = models.IntegerField()
    qtd_vendas = models.IntegerField()
    em_atividade = models.BooleanField(default=False)
    mesas_atendidas = models.ManyToManyField(Mesa)
    turno = models.CharField(max_length=100)
    horario_entrada = models.DateTimeField()
    horario_saida = models.DateTimeField()

    
    
#Python: Select Interpreter