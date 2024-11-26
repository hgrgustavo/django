from django.forms import ModelForm, TextInput, Select

from website.models import Tarefa, Usuario


class CadastroTarefaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Tarefa
        fields = [
            "tar_descricao",
            "tar_setor",
            "usu_codigo",
            "tar_prioridade"
        ]
        widgets = {
            "tar_descricao": TextInput(attrs={"placeholder": "Descrição", "required": "required"}),
            "tar_setor": TextInput(attrs={"placeholder": "Setor", "required": "required"}),
            "usu_codigo": Select(choices=[
                ("", "Usuário"),
                (1, "Gus")
                # query users name with the respective fk
            ], attrs={
                "required": "required",
                "onchange": "this.options[0].hidden=false; this.options[0].disabled=true; this.options.selected=true;"
            }),

            "tar_prioridade": Select(choices=[
                ("", "Prioridade"),
                ("Alta", "Alta"),
                ("Média", "Média"),
                ("Baixa", "Baixa")
            ], attrs={
                "required": "required",
                "onchange": "this.options[0].hidden=false; this.options[0].disabled=true; this.options.selected=true;"
            })
        }


class CadastroUsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""

    class Meta:
        model = Usuario
        fields = [
            "usu_nome",
            "usu_email"
        ]
        widgets = {
            "usu_nome": TextInput(attrs={"placeholder": "Nome", "required": "required"}),
            "usu_email": TextInput(attrs={"placeholder": "Email", "required": "required"})
        }
