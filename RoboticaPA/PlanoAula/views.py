from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

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
