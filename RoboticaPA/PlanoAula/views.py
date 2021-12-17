from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from PlanoAula.models import PlanoAula

class Criar(CreateView):
    model = PlanoAula
    fields = ['titulo', 'contextualizacao', 'descricao_atividade']
    template_name = 'PlanoAula/criar.html'
    success_url = reverse_lazy('plano_aula:listar')

    # Cria no HTML um objeto "form"

def listar(request):
    planos_aula = PlanoAula.objects.all()

    informacoes = {
        'lista_planos_aula': planos_aula
    }

    return render(request, "PlanoAula/listar.html", informacoes)

class EditarAula(LoginRequiredMixin, generic.UpdateView):
    model = PlanoAula
    form_class = forms.FormEditarPlano_aula
    template_name = 'Plano_aula/editar.html'
    success_url = reverse_lazy('plano_aula:listar')


class DetalhesPlanoAula(LoginRequiredMixin, generic.DetailView):
    model = PlanoAula
    template_name = "Plano_aula/detalhes.html"
