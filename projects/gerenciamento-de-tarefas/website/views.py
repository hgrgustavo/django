from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from website.forms import CadastroTarefaForm, CadastroUsuarioForm
from website.models import Tarefa, Usuario


class CadastroTarefas(CreateView):
    model = Tarefa
    template_name = "cadastro_tarefas.html"
    form_class = CadastroTarefaForm
    success_url = reverse_lazy("tarefas/cadastro/")


class CadastroUsuarios(CreateView):
    model = Usuario
    template_name = "cadastro_usuarios.html"
    form_class = CadastroUsuarioForm
    sucess_url = reverse_lazy("usuario/cadastro/")


class MinhasTarefas(ListView):
    template_name = "minhas_tarefas.html"
    model = Tarefa
    context_object_name = "tarefas"


class EmptyPathView(TemplateView):
    template_name = "base.html"


class ExcluirTarefa(DeleteView):
    model = Tarefa
    success_url = reverse_lazy("website:minhas_tarefas")
