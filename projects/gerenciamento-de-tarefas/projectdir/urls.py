from django.urls import path
from website import views


urlpatterns = [
    path('cadastro-usuario/', views.CadastroUsuarios.as_view(), name='cadastro_usuarios'),
    path("painel/", views.MinhasTarefas.as_view(), name="minhas_tarefas"),
    path("cadastro-tarefa/", views.CadastroTarefas.as_view(), name="cadastro_tarefas"),

    # login path


    # empty path
    path("", views.EmptyPathView.as_view())
]

