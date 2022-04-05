from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from Disciplina.models import Disciplina, Conteudo, SugestaoDisciplina, SugestaoConteudo

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
