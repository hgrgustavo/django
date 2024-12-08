from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView

from website.forms import CadastroTarefaForm, CadastroUsuarioForm
from website.models import Tarefa, Usuario


class CadastroTarefas(CreateView):
    model = Tarefa
    template_name = 'cadastro_tarefas.html'
    form_class = CadastroTarefaForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success_url')  # Replace 'success_url' with your actual success URL
        return render(request, self.template_name, {"form": form})


class CadastroUsuarios(CreateView):
    model = Usuario
    template_name = "cadastro_usuarios.html"
    form_class = CadastroUsuarioForm
    sucess_url = "usuario/cadastro/"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect(self.sucess_url)  # Replace 'success_url' with your actual success URL
        return render(request, self.template_name, {"form": form})


class MinhasTarefas(ListView):
    template_name = "minhas_tarefas.html"
    paginate_by = 3
    model = Tarefa
    context_object_name = "tarefas"


class EmptyPathView(TemplateView):
    template_name = "base.html"
