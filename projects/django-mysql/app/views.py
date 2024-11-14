from django.views.generic import CreateView, ListView
from . import models
from . import forms


# FORMULÁRIO DE USUÁRIOS
# ----------------------------------------------
class CriarUsuario(CreateView):
    template_name = "cadastro_usuario.html"
    model = models.TblUsuario
    form_class = forms.FormUsuario


# FORMULÁRIO DE TAREFAS
# ----------------------------------------------
class CriarTarefa(CreateView):
    template_name = "cadastro_tarefas.html"
    model = models.TblTarefas
    form_class = forms.FormTarefa


# PAINEL DE TAREFAS
# ----------------------------------------------
class GerenciarTarefa(ListView):
    template_name = "gerenciar_tarefas.html"
    model = models.TblTarefas