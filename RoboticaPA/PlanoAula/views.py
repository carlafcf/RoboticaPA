from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
import datetime

from PlanoAula.models import PlanoAula
from Usuario.models import Usuario
from PlanoAula import forms


class Criar(generic.CreateView, LoginRequiredMixin):
    model = PlanoAula
    fields = ['titulo', 'contextualizacao', 'descricao_atividade']
    template_name = 'PlanoAula/criar.html'
    success_url = reverse_lazy('plano_aula:listar')

    def form_valid(self, form):
        usuario = Usuario.objects.get(username=self.request.user.username)
        form.instance.responsavel = usuario
        return super().form_valid(form)

    # Cria no HTML um objeto "form"

@login_required
def listar(request):
    planos_aula = PlanoAula.objects.all()

    informacoes = {
        'lista_planos_aula': planos_aula
    }

    return render(request, "PlanoAula/listar.html", informacoes)

class Editar(generic.UpdateView):
        model = PlanoAula
        form_class = forms.FormEditarPlano_aula
        template_name = 'PlanoAula/editar.html'
        success_url = reverse_lazy('plano_aula:listar')
        fieelds = ["titulo", "contextualizacao", "descricao_atividade"]

#class Detalhe(generic.DetailView):
 #   model = PlanoAula
  #  template_name = "PlanoAula/detalhes.html"        

class Deletar(generic.DeleteView):
        model = PlanoAula
        template_name = 'PlanoAula/deletar.html'
        success_url = reverse_lazy('plano_aula:listar')

