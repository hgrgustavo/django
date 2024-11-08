from django.db import models


class Usuario(models.Model):
    class Admin:

        pass

    def __str__(self):

        return self.email
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)


class Colecao(models.Model):
    class Admin:

        pass

    def __str__(self):

        return self.nome
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)


class Livro(models.Model):
    class Admin:

        list_display = ('colecao_id', 'nome', 'capa', 'genero', 'autor', 'editora')
    list_filter = ['ano_public']
    search_fields = ['nome']

    def __str__(self):

        return self.nome
    colecao_id = models.ForeignKey(Colecao, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    capa = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano_public = models.DateField('Ano de publicacao')


class Comentario(models.Model):
    class Admin:

        pass

    def __str__(self):

        return self.nome
    livro_id = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    texto = models.TextField(max_length=255)
