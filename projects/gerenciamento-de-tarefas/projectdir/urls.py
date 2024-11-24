from django.urls import path
from website import views


urlpatterns = [
    path("cadastro_usuarios.html", views.CadastroUsuarios.as_view()),
    path("cadastro_tarefas.html", views.CadastroTarefas.as_view()),
    path("minhas_tarefas.html", views.MinhasTarefas.as_view()),

    # login path


    # empty path
    path("", views.EmptyPathView.as_view())
]
