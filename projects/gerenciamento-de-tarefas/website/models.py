from django.db import models


class Usuario(models.Model):
    usu_codigo = models.BigAutoField(primary_key=True)
    usu_nome = models.CharField(max_length=255)
    usu_email = models.EmailField(max_length=255)


class Tarefa(models.Model):
    tar_codigo = models.BigAutoField(primary_key=True)
    tar_descricao = models.CharField(max_length=255)
    tar_setor = models.CharField(max_length=255)
    tar_prioridade = models.CharField(max_length=20, choices=[("Alta", "Alta"), ("Média", "Média"), ("Baixa", "Baixa")])
    tar_status = models.CharField(max_length=20, choices=[("Completa", "Completa"), ("Pendente", "Pendente")])
    tar_data = models.DateField()

    usu_codigo = models.ForeignKey(Usuario, on_delete=models.CASCADE)