from django.forms import ModelForm, modelformset_factory, TextInput, Select

from . import models


class CadastroUsuarioForm(ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["usu_nome", "usu_email"]


CadastroUsuarioFormSet = modelformset_factory(models.Usuario, form=CadastroUsuarioForm,
    fields=["usu_nome", "usu_email"],
    widgets={"usu_nome": TextInput(attrs={"placeholder": "Nome", "required": "required"}),
        "usu_email": TextInput(attrs={"placeholder": "Email", "required": "required"})
    }
)


class CadastroTarefaForm(ModelForm):
    class Meta:
        model = models.Tarefa
        fields = ["tar_descricao", "tar_setor", "usu_codigo", "tar_prioridade"]


CadastroTarefaFormSet = modelformset_factory(models.Tarefa, CadastroTarefaForm,
    fields=["tar_descricao", "tar_setor", "usu_codigo", "tar_prioridade"],
    widgets={"tar_descricao": TextInput(attrs={"placeholder": "Descrição", "required": "required"}),
        "tar_setor": TextInput(attrs={"placeholder": "Setor", "required": "required"}),
        "usu_codigo": Select(attrs={"required": "required"}),
        "tar_prioridade": Select(attrs={"required": "required"})
    }
)
