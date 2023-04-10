from audioop import reverse
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse 
import datetime

from django.urls import reverse_lazy
from django.views import generic
from Disciplina.models import Disciplina, Conteudo
from PlanoAula.models import PlanoAula, LikePlanoAula, ExecucaoPlanoAula
from Usuario.models import Usuario
from PlanoAula import forms

@login_required
def home(request):

    if (not request.user.first_name or not request.user.last_name):
        return redirect('usuario:completar_cadastro', pk = request.user.pk)
    
    planos_aula = PlanoAula.objects.all()
    conteudos = list(Conteudo.objects.filter(status='Ativo'))
    disciplinas = list(Disciplina.objects.filter(status='Ativo'))

    inf_disciplinas = encontrar_planos_aula_disciplina(planos_aula, disciplinas)
    principais_conteudos = encontrar_principais_conteudos(likes_execucao_por_conteudo(planos_aula, conteudos), 5)
    principais_planos_aula = encontrar_principais_planos_aula(planos_aula, 5)

    informacoes = {
        'lista_planos_aula': planos_aula[:10],
        'principais_conteudos': principais_conteudos,
        'principais_planos_aula': principais_planos_aula,
        'inf_disciplinas': inf_disciplinas
    }

    return render(request, "home.html", informacoes)

    # return render(request, "Base/home.html")

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
        form_programacao = forms.FormProgramacao(request.POST, request.FILES)
        form_midias_robo = forms.FormMidiasRobo(request.POST, request.FILES)
        form_midias_execucao = forms.FormMidiasExecucao(request.POST, request.FILES)
        if (form_inf_gerais.is_valid() and form_montagem.is_valid() and form_programacao.is_valid()
                and form_midias_robo.is_valid() and form_midias_execucao.is_valid()):

            conteudos = request.POST.get('lista_id_conteudos','').split(',')

            plano_aula = PlanoAula()
            plano_aula.responsavel = Usuario.objects.get(id=request.user.id)

            # Informações gerais
            plano_aula.titulo = form_inf_gerais.cleaned_data['titulo']
            plano_aula.contextualizacao = form_inf_gerais.cleaned_data['contextualizacao']
            plano_aula.descricao_atividade = form_inf_gerais.cleaned_data['descricao_atividade']
            if (form_inf_gerais.cleaned_data['avaliacao'] != ""):
                plano_aula.avaliacao = form_inf_gerais.cleaned_data['avaliacao']

            # Montagem
            plano_aula.robo_equipamento = form_montagem.cleaned_data['robo_equipamento']
            plano_aula.robo_descricao = form_montagem.cleaned_data['robo_descricao']
            if (form_montagem.cleaned_data['robo_link'] != ""):
                plano_aula.robo_link = form_montagem.cleaned_data['robo_link']

            # Programação
            plano_aula.prog_linguagem = form_programacao.cleaned_data['prog_linguagem']
            plano_aula.prog_descricao = form_programacao.cleaned_data['prog_descricao']
            if (form_programacao.cleaned_data['prog_link'] != ""):
                plano_aula.prog_link = form_programacao.cleaned_data['prog_link']
            if (form_programacao.cleaned_data['prog_codigos'] != ""):
                plano_aula.prog_codigos = form_programacao.cleaned_data['prog_codigos']
            
            # Midias robo
            if (form_midias_robo.cleaned_data['robo_fotos'] != ""):
                plano_aula.robo_fotos = form_midias_robo.cleaned_data['robo_fotos']
            if (form_midias_robo.cleaned_data['robo_videos'] != ""):
                plano_aula.robo_videos = form_midias_robo.cleaned_data['robo_videos']
            if (form_midias_robo.cleaned_data['robo_pdf'] != ""):
                plano_aula.robo_pdf = form_midias_robo.cleaned_data['robo_pdf']

            # Midias execução
            if (form_midias_execucao.cleaned_data['exec_fotos'] != ""):
                plano_aula.exec_fotos = form_midias_execucao.cleaned_data['exec_fotos']
            if (form_midias_execucao.cleaned_data['exec_videos'] != ""):
                plano_aula.exec_videos = form_midias_execucao.cleaned_data['exec_videos']

            # Salvar
            plano_aula.save()

            # Adicionar conteúdos
            for conteudo in conteudos:
                plano_aula.conteudos.add(Conteudo.objects.get(id=int(conteudo)))
            
            plano_aula.save()

            return redirect('plano_aula:listar')
    else:
        form_inf_gerais = forms.FormInfGerais()
        form_montagem = forms.FormMontagem()
        form_programacao = forms.FormProgramacao()
        form_midias_robo = forms.FormMidiasRobo()
        form_midias_execucao = forms.FormMidiasExecucao()
        lista_disciplinas = Disciplina.objects.filter(status="Ativo")
        lista_conteudos = Conteudo.objects.filter(status="Ativo")
        informacoes = {
            'form_inf_gerais': form_inf_gerais,
            'form_montagem': form_montagem,
            'form_programacao': form_programacao,
            'form_midias_robo': form_midias_robo,
            'form_midias_execucao': form_midias_execucao,
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

@login_required
def listar_todos(request):
    planos_aula = PlanoAula.objects.all()

    informacoes = {
        'lista_planos_aula': planos_aula
    }

    return render(request, "PlanoAula/listar.html", informacoes)

class ListarTodos(generic.ListView):
    model = PlanoAula
    template_name = 'PlanoAula/listar.html'
    context_object_name = 'lista_planos_aula'
    paginate_by = 15

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

def likes_execucao_por_conteudo(planos_aula, conteudos):
    likes = LikePlanoAula.objects.all()
    execucoes = ExecucaoPlanoAula.objects.all()

    inf_conteudos = []

    for conteudo in conteudos:
        informacoes = []
        informacoes.append(conteudo)
        informacoes.append(0)
        inf_conteudos.append(informacoes)

    for plano_aula in planos_aula:
        likes = list(LikePlanoAula.objects.filter(plano_aula=plano_aula).values_list('usuario', flat=True))
        execucoes = list(ExecucaoPlanoAula.objects.filter(plano_aula=plano_aula).values_list('usuario', flat=True))
        quantidade_likes_execucoes = len(set(likes + execucoes))
        for indice, conteudo in enumerate(conteudos):
            if conteudo in plano_aula.conteudos.all():
                inf_conteudos[indice][1] += quantidade_likes_execucoes
    
    return inf_conteudos

def encontrar_principais_planos_aula(planos_aula, quantidade):

    inf_planos_aula = []

    for plano_aula in planos_aula:
        likes = list(LikePlanoAula.objects.filter(plano_aula=plano_aula).values_list('usuario', flat=True))
        execucoes = list(ExecucaoPlanoAula.objects.filter(plano_aula=plano_aula).values_list('usuario', flat=True))
        quantidade_likes_execucoes = len(set(likes + execucoes))
        inf_planos_aula.append([plano_aula, quantidade_likes_execucoes])
    
    inf_planos_aula.sort(key = lambda x: x[1], reverse=True)
    
    return inf_planos_aula[0:quantidade]

def encontrar_principais_conteudos(inf_conteudos, quantidade):
    inf_conteudos.sort(key = lambda x: x[1], reverse=True)
    return inf_conteudos[0:quantidade]

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

class Detalhe(generic.DetailView):
   model = PlanoAula
   template_name = "PlanoAula/detalhes.html"
   context_object_name = "plano_aula"

class Deletar(generic.DeleteView):
    model = PlanoAula
    template_name = 'PlanoAula/deletar.html'
    success_url = reverse_lazy('plano_aula:listar')

class Programacao(generic.DetailView):
   model = PlanoAula
   template_name = "PlanoAula/programacao.html"
   context_object_name = "plano_aula"

