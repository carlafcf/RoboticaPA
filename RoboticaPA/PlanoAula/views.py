from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from PlanoAula.models import PlanoAula

def home(request):
    if (not request.user.first_name or not request.user.last_name):
        return redirect('usuario:editar', pk = request.user.pk)
    return render(request, "home.html")

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
