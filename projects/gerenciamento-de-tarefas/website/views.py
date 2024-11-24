from django.views.generic import TemplateView, FormView
from website.models import Usuario, Tarefa
from website.forms import CadastroTarefaForm


class CadastroTarefas(FormView):
    context_object_name = "tarefa_object_list"




class EmptyPathView(TemplateView):
    template_name = "base.html"

