from django.views.generic import TemplateView, CreateView, ListView

from website.forms import CadastroTarefaForm
from website.models import Tarefa


class CadastroTarefas(CreateView):
    context_object_name = "tarefa_object_list"
    model = Tarefa
    template_name = "cadastro_tarefas.html"
    form_class = CadastroTarefaForm


class CadastroUsuarios(CreateView):
    template_name = "cadastro_usuarios.html"


class MinhasTarefas(ListView):
    template_name = "minhas_tarefas.html"


class EmptyPathView(TemplateView):
    template_name = "base.html"
