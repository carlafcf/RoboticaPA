from django import forms
from django.forms import ModelForm

from Acoes.models import MensagemAcoes

class FormNovaMensagem(ModelForm):

    class Meta:
        model = MensagemAcoes
        fields = ('texto',)
    
    def save(self, commit=True):
        instance = super(FormNovaMensagem, self).save(commit=False)
        
        if commit:
            instance.save()
        return instance