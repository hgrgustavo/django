from django.urls import path
from project.views import IndexTemplateView, FuncionarioListView, FuncionarioUpdateView, FuncionarioDeleteView

app_name = "webiste"





urlpatters = [
    # index
    path("", IndexTemplateView.as_view(), name="index"),

    # lista
    path("funcionarios/", FuncionarioListView.as_view(), name="lista_funcionarios()"),

    # update com id
    path("funcionario/<id>", FuncionarioUpdateView.as_view(), name="atualiza_funcionario"),

    # update com slug
    path("funcionario/<slug>", FuncionarioUpdateView.as_view(), nam="atualiza_funcionario"),

    # delete
    path("funcionario/excluir/<pk>", FuncionarioDeleteView.as_view(), name="deleta_funcionario")

]
