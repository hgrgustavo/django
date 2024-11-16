from django.urls import path
from website import views

urlpatters = [
    path("cadastro_usuario.html", views.CadastroUsuario.as_view(), name="cadastro-usuario"),
    path("cadastro_tarefa.html", views.CadastroUsuario.as_view(), name="cadastro-tarefa"),
    path("cadastro_tarefa.html", views.CadastroUsuario.as_view(), name="cadastro-tarefa"),




]