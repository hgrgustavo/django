from django.urls import path
from website import views


urlpatterns = [
    path("", views.CadastroUsuario.as_view()),
    path("/cadastro_tarefas.html", views.CadastroTarefas.as_view()),
    path("/minhas_tarefas.html", views.MinhasTarefas.as_view()),

]
