from django.db import models
from django.urls import reverse


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return f'{self.nome} - Estoque {self.estoque}'

    class Meta:
        db_table = "produto"


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    class Meta:
        db_table = "cliente"