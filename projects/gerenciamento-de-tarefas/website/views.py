from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from website.models import Usuario, Tarefa


class CadastroUsuario(CreateView):
    template_name = "cadastro_usuario.html"
    model = Usuario
    fields = ["usu_nome", "usu_email"]
    success_url = "minhas_tarefas.html"



class CadastroTarefas(CreateView):
    template_name = "cadastro_tarefas.html"
    model = Tarefa
    fields = ["tar_descricao", "tar_setor", "usu_codigo", "tar_prioridade"]
    success_url = "minhas_tarefas.html"


class MinhasTarefas(ListView):
    template_name = "minhas_tarefas.html"
    model = Tarefa
    paginate_by = 3

