from django.urls import path
from website import views


urlpatterns = [
    path("tarefas/cadastro/", views.CadastroTarefas.as_view(), name="cadastro_tarefas"),
    path("usuarios/cadastro/", views.CadastroUsuarios.as_view(), name="cadastro_usuarios"),
    path("tarefas/minhas-tarefas/", views.MinhasTarefas.as_view(), name="minhas_tarefas"),
    path("tarefas/minhas-tarefas/excluir", views.ExcluirTarefa.as_view(), name="excluir_tarefa"),


    # login path


    # empty path
    path("", views.EmptyPathView.as_view())
]

