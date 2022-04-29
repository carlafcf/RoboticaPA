from django.shortcuts import render
from django.http import HttpResponse
import json

from django.views import generic
from django.urls import reverse_lazy

from Disciplina.models import Disciplina, Conteudo, SugestaoDisciplina, SugestaoConteudo
from Usuario.models import Usuario

# class CriarDisciplina(generic.CreateView):
#     model = Disciplina
#     fields = ['name']
#     template_name = "Disciplina/criar.html"
#     success_url = reverse_lazy('plano_aula:listar')


def listar(request):
    disciplinas = Disciplina.objects.all()
    conteudos = Conteudo.objects.all()

    informacoes = {
        'lista_disciplinas': disciplinas,
        'lista_conteudos': conteudos,
    }

    return render(request, "Disciplina/listar.html", informacoes)

def sugerir_disciplina(request):
    nome = request.GET.get('nome')
    usuario = Usuario.objects.get(username=request.user.username)
    sugestao_disciplina = SugestaoDisciplina(nome = nome, usuario = usuario)
    sugestao_disciplina.save()
    
    response_data = 'successful!'

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

def sugerir_conteudo(request):
    nome = request.GET.get('nome')
    nome_disciplina = request.GET.get('disciplina')
    usuario = Usuario.objects.get(username=request.user.username)
    disciplina = Disciplina.objects.get(nome = nome_disciplina)
    sugestao_conteudo = SugestaoConteudo(nome = nome, usuario = usuario, disciplina = disciplina)
    sugestao_conteudo.save()
    
    response_data = 'successful!'

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
