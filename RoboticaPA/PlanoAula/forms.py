from django.contrib.auth import forms as auth_forms
from django import forms
from django.forms import ModelForm

from RoboticaPA.RoboticaPA.PlanoAula.models import PlanoAula

class FormEditarPlano_aula(ModelForm):

    class Meta:
        model = PlanoAula
        fields = ('titulo', 'descricao', 'atividade')


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(FormEditarPlano_aula, self).save(commit=False)
        # user.active = False # send confirmation email
        if commit:
            user.save()
        return user