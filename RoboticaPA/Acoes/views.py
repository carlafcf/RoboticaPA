from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import FormMixin
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse 
import json

from Acoes.models import Acoes, Midia, MensagemAcoes
from Acoes.forms import FormNovaMensagem, FormNovaMidia
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
    
    def get_context_data(self,**kwargs):
        context = super(EditarAcao,self).get_context_data(**kwargs)
        midias_acao = Midia.objects.filter(acao__id = self.kwargs['pk'])
        context['midias_acao'] = midias_acao
        context['form_nova_midia'] = FormNovaMidia()
        return context

class DetalhesAcao(FormMixin, generic.DetailView):
    model = Acoes
    template_name = 'Acoes/detalhes.html'
    context_object_name = 'acao'
    form_class = FormNovaMensagem

    def get_success_url(self):
        return reverse('acoes:detalhes', kwargs={'pk': self.object.id})

    def get_context_data(self,**kwargs):
        context = super(DetalhesAcao,self).get_context_data(**kwargs)
        lista_mensagens = MensagemAcoes.objects.filter(acao__id = self.kwargs['pk'], mensagem_original = None)
        context['lista_mensagens'] = lista_mensagens
        context['form_nome_mensagem'] = FormNovaMensagem()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        usuario = Usuario.objects.get(pk=self.request.user.pk)
        acao = Acoes.objects.get(pk=self.object.id)

        form.instance.usuario = usuario
        form.instance.acao = acao
        if (self.request.POST.get('mensagem_original') != ""):
            mensagem_original = MensagemAcoes.objects.get(pk=self.request.POST.get('mensagem_original'))
            form.instance.mensagem_original = mensagem_original

        form.save()
        return super(DetalhesAcao, self).form_valid(form)

def deletar(request, pk):
    acao = Acoes.objects.get(pk=pk)
    acao.deletada = True
    acao.save()

    return redirect('acoes:listar')

def deletar_mensagem(request, pk):
    mensagem = MensagemAcoes.objects.get(id=pk)
    acao_id = mensagem.acao.id
    mensagem.delete()

    return HttpResponseRedirect(reverse('acoes:detalhes', kwargs={'pk': acao_id}))
    
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
