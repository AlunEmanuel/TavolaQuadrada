from django import forms
from .models import Mesa

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['nome', 'descricao', 'numero_max_jogadores', 'categoria']
