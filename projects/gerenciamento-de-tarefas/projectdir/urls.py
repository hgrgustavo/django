from django.urls import path
from website import views


urlpatterns = [
    path("usuarios/cadastro/", views.CadastroUsuarios.as_view(), name="cadastro_usuarios"),
    path("tarefas/minhas-tarefas/", views.MinhasTarefas.as_view(), name="minhas_tarefas"),
    path("tarefas/cadastro/", views.CadastroTarefas.as_view(), name="cadastro_tarefas"),

    # login path


    # empty path
    path("", views.EmptyPathView.as_view())
]

