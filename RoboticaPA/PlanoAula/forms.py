from django.contrib.auth import forms as auth_forms
from django import forms
from django.forms import ModelForm

from PlanoAula.models import PlanoAula

class FormCriarPlano_aula(ModelForm):

    class Meta:
        model = PlanoAula
        fields = ('titulo', 'contextualizacao', 'descricao_atividade')


class FormEditarPlano_aula(ModelForm):
    titulo = forms.CharField(max_length=200, label='Titulo', widget=forms.Textarea)
    contextualizacao = forms.CharField(max_length=200, label='Contextualizacao', widget=forms.Textarea)
    descricao_atividade = forms.CharField(max_length=200, label='descricao da atividade', widget=forms.Textarea)
    #password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    class Meta:
        model = PlanoAula
        fields = ('titulo', 'contextualizacao', 'descricao_atividade')



    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(FormEditarPlano_aula, self).save(commit=False)

        #user.set_password(self.cleaned_data["password1"])
        # user.active = False # send confirmation email
        if commit:
            user.save()
        return user
