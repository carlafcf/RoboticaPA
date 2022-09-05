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
        form_inf_gerais = forms.FormInfGerais(request.POST)
        form_montagem = forms.FormMontagem(request.POST)
        form_programacao = forms.FormProgramacao(request.POST)
        if (form_inf_gerais.is_valid() and form_montagem.is_valid() and form_programacao.is_valid()):

            conteudos = request.POST.get('lista_id_conteudos','').split(',')

            plano_aula = PlanoAula()
            plano_aula.responsavel = Usuario.objects.get(id=request.user.id)
            plano_aula.titulo = form_inf_gerais.cleaned_data['titulo']
            plano_aula.contextualizacao = form_inf_gerais.cleaned_data['contextualizacao']
            plano_aula.descricao_atividade = form_inf_gerais.cleaned_data['descricao_atividade']
            if (form_inf_gerais.cleaned_data['avaliacao'] != ""):
                plano_aula.avaliacao = form_inf_gerais.cleaned_data['avaliacao']
            plano_aula.robo_equipamento = form_montagem.cleaned_data['robo_equipamento']
            plano_aula.robo_descricao = form_montagem.cleaned_data['robo_descricao']
            if (form_montagem.cleaned_data['robo_link'] != ""):
                plano_aula.robo_link = form_montagem.cleaned_data['robo_link']
            plano_aula.prog_linguagem = form_programacao.cleaned_data['prog_linguagem']
            plano_aula.prog_descricao = form_programacao.cleaned_data['prog_descricao']
            if (form_programacao.cleaned_data['prog_link'] != ""):
                plano_aula.prog_link = form_programacao.cleaned_data['prog_link']
            plano_aula.save()

            for conteudo in conteudos:
                plano_aula.conteudos.add(Conteudo.objects.get(id=int(conteudo)))
            
            plano_aula.save()

            return redirect('plano_aula:listar')
    else:
        form_inf_gerais = forms.FormInfGerais()
        form_montagem = forms.FormMontagem()
        form_programacao = forms.FormProgramacao()
        lista_disciplinas = Disciplina.objects.filter(status="Ativo")
        lista_conteudos = Conteudo.objects.filter(status="Ativo")
        informacoes = {
            'form_inf_gerais': form_inf_gerais,
            'form_montagem': form_montagem,
            'form_programacao': form_programacao,
            'lista_disciplinas': lista_disciplinas,
            'lista_conteudos': lista_conteudos,
        }

        return render(request, "PlanoAula/criar.html", informacoes)


@login_required
def listar(request):
    planos_aula = PlanoAula.objects.all()
    principais_conteudos = Conteudo.objects.filter(status='Ativos')
    disciplinas = list(Disciplina.objects.filter(status='Ativo'))

    inf_disciplinas = encontrar_planos_aula_disciplina(planos_aula, disciplinas)

    encontrar_principais_conteudos(disciplinas)

    informacoes = {
        'lista_planos_aula': planos_aula[:10],
        'principais_conteudos': principais_conteudos,
        'inf_disciplinas': inf_disciplinas
    }

    return render(request, "PlanoAula/listar.html", informacoes)

def encontrar_planos_aula_disciplina(planos_aula, disciplinas):

    inf_disciplinas = []

    for disciplina in disciplinas:
        informacoes = []
        informacoes.append(disciplina)
        informacoes.append(0)
        inf_disciplinas.append(informacoes)

    for plano_aula in planos_aula:
        disciplinas_pa = []
        for conteudo in plano_aula.conteudos.all():
            if conteudo.disciplina not in disciplinas_pa:
                disciplinas_pa.append(conteudo.disciplina)
        for disciplina in disciplinas_pa:
            indice = disciplinas.index(disciplina)
            inf_disciplinas[indice][1] += 1
    
    return inf_disciplinas

def encontrar_principais_conteudos(disciplinas):
    conteudos = Conteudo.objects.filter(status='Ativo')

    qnt_planos_aula = []
    for conteudo in conteudos:
        qnt_planos_aula.append(len(conteudo.planos_de_aula.all()))
    
    print(conteudos)
    print(qnt_planos_aula)


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

