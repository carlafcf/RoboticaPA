from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse 
import json

from Acoes.models import Acoes, Midia, MensagemAcoes
from Usuario.models import Usuario
from Acoes.filters import AcoesFiltro

class CriarAcao(generic.CreateView):
    model = Acoes
    fields = ['titulo', 'tipo', 'data_inicio', 'data_fim', 'local', 'descricao']
    template_name = "Acoes/criar.html"

    def form_valid(self, form):
        usuario = Usuario.objects.get(id=self.request.user.id)
        form.instance.responsavel = usuario
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('acoes:listar_usuario', kwargs={'pk': self.request.user.id})

class EditarAcao(generic.UpdateView):
    model = Acoes
    fields = ['titulo', 'tipo', 'data_inicio', 'data_fim', 'local', 'descricao', 'status']
    template_name = "Acoes/editar.html"

    def form_valid(self, form):
        usuario = Usuario.objects.get(id=self.request.user.id)
        form.instance.responsavel = usuario
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('acoes:listar_usuario', kwargs={'pk': self.request.user.id})

class DetalhesAcao(generic.DetailView):
    model = Acoes
    template_name = 'Acoes/detalhes.html'
    context_object_name = 'acao'

    def get_context_data(self,**kwargs):
        context = super(DetalhesAcao,self).get_context_data(**kwargs)
        lista_mensagens = MensagemAcoes.objects.filter(acao__id = self.kwargs['pk'])
        context['lista_mensagens'] = lista_mensagens
        return context

def deletar(request, pk):
    acao = Acoes.objects.get(pk=pk)
    acao.deletada = True
    acao.save()

    return redirect('acoes:listar')
    
class ListarTodasAcoes(generic.ListView):
    model = Acoes
    template_name = 'Acoes/listar.html'
    context_object_name = 'lista_acoes'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        acoes_filtradas = AcoesFiltro(self.request.GET, queryset=Acoes.objects.filter(deletada=False))
        qs_filtrada = acoes_filtradas.qs
        return qs_filtrada

    def get_context_data(self,**kwargs):
        context = super(ListarTodasAcoes,self).get_context_data(**kwargs)
        acoes_filtradas = AcoesFiltro(self.request.GET, queryset=Acoes.objects.filter(deletada=False))
        context['acoes_filtradas'] = acoes_filtradas.qs
        context['form_filtro'] = acoes_filtradas.form
        context['exibir_todos'] = True
        return context
    
class ListarAcoesUsuario(generic.ListView):
    model = Acoes
    template_name = 'Acoes/listar.html'
    context_object_name = 'lista_acoes'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        acoes_filtradas = AcoesFiltro(self.request.GET, queryset=Acoes.objects.filter(deletada=False, responsavel__id = self.kwargs['pk']))
        qs_filtrada = acoes_filtradas.qs
        return qs_filtrada

    def get_context_data(self,**kwargs):
        context = super(ListarAcoesUsuario,self).get_context_data(**kwargs)
        acoes_filtradas = AcoesFiltro(self.request.GET, queryset=Acoes.objects.filter(deletada=False, responsavel__id = self.kwargs['pk']))
        context['acoes_filtradas'] = acoes_filtradas.qs
        context['form_filtro'] = acoes_filtradas.form
        context['exibir_todos'] = False
        return context

def alterar_status_acao(request, pk):
    acao = Acoes.objects.get(pk=pk)
    acao.status = not acao.status
    acao.save()
    return finalizar_requisicao_api(acao.status)

def finalizar_requisicao_api(response_data):
    response_data = response_data

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
