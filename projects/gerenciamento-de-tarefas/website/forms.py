from django.forms import modelformset_factory, ModelForm
from website.models import Tarefa, Usuario


class CadastroTarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = [
            "tar_descricao",
            "tar_setor",
            "usu_codigo",
            "tar_prioridade"
        ]

