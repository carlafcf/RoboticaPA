from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

from django.views import generic
from django.urls import reverse_lazy

from django.views.decorators.csrf import csrf_exempt

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

def listar_sugestoes(request):
    sugestoes_disciplina = SugestaoDisciplina.objects.filter(status="A")
    sugestoes_conteudo = SugestaoConteudo.objects.filter(status="A")
    disciplinas = Disciplina.objects.all()
    conteudos = Conteudo.objects.all()

    informacoes = {
        'sugestoes_disciplina': sugestoes_disciplina,
        'sugestoes_conteudo': sugestoes_conteudo,
        'lista_disciplinas': disciplinas,
        'lista_conteudos': conteudos,
    }

    return render(request, "Disciplina/listar_sugestoes.html", informacoes)

@csrf_exempt
def analisar_sugestoes_disciplina(request):
    print("aqui!!")
    lista_disciplinas_aceitas = request.POST.getlist('lista_disciplinas_aceitas[]')
    lista_disciplinas_negadas = request.POST.getlist('lista_disciplinas_negadas[]')

    for pk in lista_disciplinas_aceitas:
        sugestao = SugestaoDisciplina.objects.get(id=int(pk))
        nova_disciplina = Disciplina(nome = sugestao.nome)
        nova_disciplina.save()
        sugestao.status = 'B'
        sugestao.save()
    
    for pk in lista_disciplinas_negadas:
        sugestao = SugestaoDisciplina.objects.get(id=int(pk))
        sugestao.status = 'C'
        sugestao.save()

    return redirect('disciplina:listar_sugestoes')

@csrf_exempt
def analisar_sugestoes_conteudo(request):
    lista_conteudos_aceitos = request.POST.getlist('lista_conteudos_aceitos[]')
    lista_conteudos_negados = request.POST.getlist('lista_conteudos_negados[]')

    for pk in lista_conteudos_aceitos:
        sugestao = SugestaoConteudo.objects.get(id=int(pk))
        novo_conteudo = Conteudo(nome = sugestao.nome, disciplina = sugestao.disciplina)
        novo_conteudo.save()
        sugestao.status = 'B'
        sugestao.save()
    
    for pk in lista_conteudos_negados:
        sugestao = SugestaoConteudo.objects.get(id=int(pk))
        sugestao.status = 'C'
        sugestao.save()

    return redirect(reverse_lazy('disciplina:listar_sugestoes'))

def sugerir_disciplina(request):
    nome = request.GET.get('nome')
    usuario = Usuario.objects.get(username=request.user.username)
    sugestao_disciplina = SugestaoDisciplina(nome = nome, usuario = usuario)
    sugestao_disciplina.save()
    
    return finalizar_requisicao_api()

def sugerir_conteudo(request):
    nome = request.GET.get('nome')
    nome_disciplina = request.GET.get('disciplina')
    usuario = Usuario.objects.get(username=request.user.username)
    disciplina = Disciplina.objects.get(nome = nome_disciplina)
    sugestao_conteudo = SugestaoConteudo(nome = nome, usuario = usuario, disciplina = disciplina)
    sugestao_conteudo.save()
    
    return finalizar_requisicao_api()

def definir_status_sugestao_disciplina(request, aceitar, id):
    sugestao_disciplina = SugestaoDisciplina.objects.get(id=id)

    if (aceitar == 1):
        sugestao_disciplina.status = "B"
        sugestao_disciplina.save()

        disciplina = Disciplina(nome = sugestao_disciplina.nome)
        disciplina.save()
    else:
        sugestao_disciplina.status = "C"
        sugestao_disciplina.save()

    return redirect('disciplina:listar_sugestoes')

def finalizar_requisicao_api():
    response_data = 'successful!'

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
