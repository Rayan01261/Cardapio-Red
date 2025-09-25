from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from cardapio.models import Mesa


class Usuario(AbstractUser):
    
    nome_completo = models.CharField(max_length=150, verbose_name="Nome")
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
    
# Rever isso, pois não acho que precise desse atributo Ativo, talvez tenha algo interessante a se colocar.
class Gerente(Usuario):
    
    class Meta:
        # db_table = "Gerente"
        # managed = True
        verbose_name = 'Gerente'
        verbose_name_plural = 'Gerentes'

class Garcom(Usuario):
    qtd_vendas = models.IntegerField()

    class Meta:
        # db_table = "Gerente "
        # managed = True
        verbose_name = 'qtd_venda'
        verbose_name_plural = 'qtd_vendas'
