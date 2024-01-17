from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from Acoes.models import Acoes, Midia, MensagemAcoes
from Usuario.models import Usuario
from Acoes.filters import AcoesFiltro

class CriarAcao(generic.CreateView):
    model = Acoes
    fields = ['titulo', 'tipo', 'data_inicio', 'data_fim', 'local', 'descricao']
    template_name = "Acoes/criar.html"
    success_url = reverse_lazy('acoes:criar')

    def form_valid(self, form):
        usuario = Usuario.objects.get(id=self.request.user.id)
        form.instance.responsavel = usuario
        return super().form_valid(form)
    
class ListarTodasAcoes(generic.ListView):
    model = Acoes
    template_name = 'Acoes/listar.html'
    context_object_name = 'lista_acoes'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        acoes_filtradas = AcoesFiltro(self.request.GET, queryset=Acoes.objects.all())
        qs_filtrada = acoes_filtradas.qs
        return qs_filtrada

    def get_context_data(self,**kwargs):
        context = super(ListarTodasAcoes,self).get_context_data(**kwargs)
        acoes_filtradas = AcoesFiltro(self.request.GET, queryset=Acoes.objects.all())
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
        acoes_filtradas = AcoesFiltro(self.request.GET, queryset=Acoes.objects.filter(responsavel__id = self.kwargs['pk']))
        qs_filtrada = acoes_filtradas.qs
        return qs_filtrada

    def get_context_data(self,**kwargs):
        context = super(ListarAcoesUsuario,self).get_context_data(**kwargs)
        acoes_filtradas = AcoesFiltro(self.request.GET, queryset=Acoes.objects.filter(responsavel__id = self.kwargs['pk']))
        context['acoes_filtradas'] = acoes_filtradas.qs
        context['form_filtro'] = acoes_filtradas.form
        context['exibir_todos'] = False
        return context

def listar_todas_acoes(request):

    informacoes = {
        'acoes_usuario': acoes_usuario,
        'todas_acoes': todas_acoes
    }

    return render(request, 'Acoes/listar.html', informacoes)

def listar_acoes_usuario(request):

    informacoes = {
        'acoes_usuario': acoes_usuario,
        'todas_acoes': todas_acoes
    }

    return render(request, 'Acoes/listar.html', informacoes)
