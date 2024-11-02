from django.db import models


# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255
    )

    sobrenome = models.CharField(
        max_length=255
    )

    cpf = models.CharField(
        max_length=14
    )

    tempo_de_servico = models.IntegerField(
        default=0
    )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    objetos = models.Manager()

