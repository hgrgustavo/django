from . import models
from django import forms

from .models import TblUsuario, TblTarefas


class FormUsuario(forms.ModelForm):
    class Meta:
        model = TblUsuario
        fields = ["usu_nome", "usu_email"]
        exclude = ["usu_codigo"]


class FormTarefa(forms.ModelForm):
    class Meta:
        model = TblTarefas
        fields = ["tar_descricao", "tar_setor", "usu_codigo", "tar_prioridade"]
        exclude = ["tar_data"]