from django.db import models


class TblUsuario(models.Model):
    usu_codigo = models.IntegerField(primary_key=True, )

    usu_nome = models.CharField(max_length=255, )

    usu_email = models.EmailField(

    )


class TblTarefas(models.Model):
    tar_codigo = models.IntegerField(primary_key=True, )

    tar_descricao = models.CharField(max_length=255, )

    tar_setor = models.CharField(max_length=255)

    tar_prioridade = models.CharField(max_length=255)

    usu_codigo = models.ForeignKey(to=TblUsuario, on_delete=models.CASCADE)

    tar_data = models.DateField(

    )
