from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from website.forms import CadastroUsuarioForm, CadastroUsuarioFormSet
from website.models import Usuario, Tarefa
from django.http import HttpResponseRedirect
from django.shortcuts import render


class CadastroUsuario(CreateView):
    template_name = "cadastro_usuario.html"
    model = Usuario
    fields = ["usu_nome", "usu_email"]
    success_url = "minhas_tarefas.html"

    def generate_form(self, request):
        return render(request, "cadastro_usuario.html", {"formset": CadastroUsuarioFormSet})





class CadastroTarefas(CreateView):
    template_name = "cadastro_tarefas.html"
    model = Tarefa
    fields = ["tar_descricao", "tar_setor", "usu_codigo", "tar_prioridade"]
    success_url = "minhas_tarefas.html"



class MinhasTarefas(ListView):
    template_name = "minhas_tarefas.html"
    model = Tarefa
    paginate_by = 3


class EmptyPathView(TemplateView):
    template_name = "base.html"

