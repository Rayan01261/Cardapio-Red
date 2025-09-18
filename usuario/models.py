from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from cardapio.models import Mesa


class Usuario(AbstractUser):
    
    mome_completo = models.CharField(max_length=150, verbose_name="Nome")
    idade = models.IntegerField(verbose_name="Idade")
    cpf = models.CharField(max_length=15, unique=True, verbose_name="CPF")
    data_nascimento = models.DateField(null=True, verbose_name="Data de nascimento")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    data_criacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        # db_table = "Usuario"
        ordering = ["data_criacao"]
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    
class Gerente(Usuario):
    ativo = models.BooleanField(default=False)
    
    class Meta:
        # db_table = "Gerente "
        # managed = True
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'

class Garcom(Usuario):
    avaliacao_estrelas = models.IntegerField()
    qtd_vendas = models.IntegerField()


