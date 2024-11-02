from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView, CreateView
from project.models import Funcionario


def lista_funcionario(request):
    funcionarios = Funcionario.objetos.all()
    contexto = {"funcionarios": funcionarios}

    return render(request, "templates/funcionarios.html", contexto)

def cria_funcionario(request, pk):
    if request.method == "POST":
        form = FormularioDeCriacao(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("lista_funcionarios"))

    else:
        return render(request, "templates/form.html", ("forms": form))



class ListaFuncionario(ListView):
    template_name = "templates/funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class FuncionarioListView(ListView):
    template_name = "website/listar.html"
    model = Funcionario
    context_object_name = "funcionarios"


class FuncionarioUpdateView(UpdateView):
    template_name = "atualiza.html"
    model = Funcionario
    fields = "__all__"

    def get_object(self, queryset=None):
        funcionario = None
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            funcionario = Funcionario.objetos.filter(id=id).first()

        elif slug is not None:
            campo_slug = self.get_slug_field()
            funcionario = Funcionario.objetos.filter(**{campo_slug: slug}).first()

        return funcionario


class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = "funcionario"
    success_url = reverse_lazy("website:lista_funcionarios")


class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionariosForm
    success_url = reverse_lazy("website:lista_funcionarios")




