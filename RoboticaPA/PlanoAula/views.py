from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from PlanoAula.models import PlanoAula

@login_required
def home(request):
    if (not request.user.first_name or not request.user.last_name):
        return redirect('usuario:completar_cadastro', pk = request.user.pk)
    return render(request, "Base/home.html")

class Criar(LoginRequiredMixin, CreateView):
    model = PlanoAula
    fields = ['titulo', 'contextualizacao', 'descricao_atividade']
    template_name = 'PlanoAula/criar.html'
    success_url = reverse_lazy('plano_aula:listar')

    # Cria no HTML um objeto "form"

@login_required
def listar(request):
    planos_aula = PlanoAula.objects.all()

    informacoes = {
        'lista_planos_aula': planos_aula
    }

    return render(request, "PlanoAula/listar.html", informacoes)
