from django.urls import path
from website import views


urlpatterns = [
    path("cadastro_usuario.html", views.CadastroUsuario.as_view(), name="cadastro-usuario"),
    path("cadastro_tarefas.html", views.CadastroTarefas.as_view(), name="cadastro-tarefa"),
    path("minhas_tarefas.html", views.MinhasTarefas.as_view(), name="minhas-tarefas"),

]
