from types import GenericAlias
from django import forms
from django.forms import Form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from PlanoAula.models import PlanoAula
from django.http import HttpResponse 
import datetime
from PlanoAula import forms



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

class Editar(UpdateView):
        model = PlanoAula
        form_class = forms.FormEditarPlano_aula
        template_name = 'PlanoAula/editar.html'
        success_url = reverse_lazy('plano_aula:listar')
        fieelds = ["titulo", "contextualizacao", "descricao_atividade"]

#class Detalhe(generic.DetailView):
 #   model = PlanoAula
  #  template_name = "PlanoAula/detalhes.html"        

class Deletar(DeleteView):
        model = PlanoAula
        template_name = 'PlanoAula/deletar.html'
        success_url = reverse_lazy('plano_aula:listar')


