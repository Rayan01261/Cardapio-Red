from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, blank=False, null=False, default='')
    
class Item(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True, blank=True)
    valor = models.DecimalField(decimal_places=2, max_digits=5)
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)

class Cardapio(models.Model):
    itens = models.ManyToManyField(Item)

class Mesa(models.Model):
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE)

class Comanda(models.Model):  
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
   
class Pedido(models.Model):
    comanda = models.ForeignKey(Comanda, related_name='pedidos', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    
class Pessoa(AbstractUser):
    
    idade = models.IntegerField(null=True, blank=True)
    cpf = models.CharField(max_length=15, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15, validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Formato de número incorreto! Formato válido: '(11) 99999-8888'. Máximo de 15 dígitos."
        )
    ])  
    
class Administrador_sistema(Pessoa):
    ativo = models.BooleanField(default=False)

class Garcom(Pessoa):  
     
    avaliacao = models.IntegerField()
    qtd_vendas = models.IntegerField()
    em_atividade = models.BooleanField(default=False)
    mesas_atendidas = models.ManyToManyField(Mesa)
    turno = models.CharField(max_length=100)
    horario_entrada = models.DateTimeField()
    horario_saida = models.DateTimeField()


#  pip install psycopg2
#  pip install psycopg2-binary

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
