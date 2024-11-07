from django import forms


class InsertEmployeeForm(forms.ModelForm):
    boss = forms.BooleanField(label="Este funcionário exerce função de chefia?", required=True)
    biography = forms.CharField(field="Biografia", required=False, widget=forms.Textarea)

    class Meta:
        fields = [
            "name",
            "last_name",
            "cpf",
            "salary"
        ]

        exclude = ["time"]