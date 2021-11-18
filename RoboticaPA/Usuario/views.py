from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView

from Usuario import forms

class CadastrarUsuario(CreateView):
    form_class = forms.FormCriarUsuario
    template_name = 'Usuario/cadastrar.html'

    # success_url = reverse_lazy('usuario:listar')