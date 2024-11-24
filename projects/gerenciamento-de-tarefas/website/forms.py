from django.forms import modelformset_factory, ModelForm, TextInput, Select
from website.models import Tarefa


class CadastroTarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = [
            "tar_descricao",
            "tar_setor",
            "usu_codigo",
            "tar_prioridade"
        ]
        modelformset = modelformset_factory(
            Tarefa,
            fields=[
                "tar_descricao",
                "tar_setor",
                "usu_codigo",
                "tar_prioridade"
            ],
            widgets={
                "tar_descricao": TextInput(attrs={"placeholder": "Descrição", "required": "required"}),
                "tar_setor": TextInput(attrs={"placeholder": "Setor", "required": "required"}),
                "usu_codigo": Select(choices=[()], attrs={"required": "required"}),
                "tar_prioridade": Select(choices=[()], attrs={"required": "required"})
            }
        )
