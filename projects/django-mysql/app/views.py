from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView


class CadastroTarefa(TemplateView):
    template_name = "cadastro_tarefa.html"


class CadastroUsuario(TemplateView):
    template_name = "cadastro_usuario.html"


class GerencimentoTarefa(ListView):
    template_name = "gerenciamento_tarefa.html"