from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse 
import datetime

from django.urls import reverse_lazy
from django.views import generic
from Disciplina.models import Disciplina, Conteudo
from PlanoAula.models import PlanoAula
from Usuario.models import Usuario
from PlanoAula import forms

@login_required
def home(request):

    if (not request.user.first_name or not request.user.last_name):
        return redirect('usuario:completar_cadastro', pk = request.user.pk)

    return render(request, "Base/home.html")

class Criar(generic.CreateView, LoginRequiredMixin):
    model = PlanoAula
    fields = ['titulo', 'contextualizacao', 'descricao_atividade', 'conteudos']
    template_name = 'PlanoAula/criar.html'
    success_url = reverse_lazy('plano_aula:listar')

    def form_valid(self, form):
        usuario = Usuario.objects.get(username=self.request.user.username)
        form.instance.responsavel = usuario
        return super().form_valid(form)

    # Cria no HTML um objeto "form"

@login_required
def criar(request):
    if (request.method == 'POST'):
        pass
    else:
        form_inf_gerais = forms.FormCriarPlano_aula()
        lista_disciplinas = Disciplina.objects.filter(status="Ativo")
        lista_conteudos = Conteudo.objects.filter(status="Ativo")
        informacoes = {
            'form_inf_gerais': form_inf_gerais,
            'lista_disciplinas': lista_disciplinas,
            'lista_conteudos': lista_conteudos,
        }

        return render(request, "PlanoAula/criar.html", informacoes)


@login_required
def listar(request):
    planos_aula = PlanoAula.objects.all()

    informacoes = {
        'lista_planos_aula': planos_aula
    }

    return render(request, "PlanoAula/listar.html", informacoes)

@login_required
def listar_usuario(request, pk):
    lista_aulas = PlanoAula.objects.filter(responsavel__pk=pk)

    informacoes = {
        'lista_aulas': lista_aulas
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

