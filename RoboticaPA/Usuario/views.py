from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

from Usuario import forms
from Usuario.models import Usuario

@login_required
def listar_ativos(request):
    lista_usuarios = Usuario.objects.filter(is_active=True)
    
    informacoes = {
        'lista_usuarios': lista_usuarios,
        'ativos': True
    }

    return render(request, "Usuario/listar.html", informacoes)

@login_required
def listar_inativos(request):
    lista_usuarios = Usuario.objects.filter(is_active=False)
    
    informacoes = {
        'lista_usuarios': lista_usuarios,
        'ativos': False
    }

    return render(request, "Usuario/listar.html", informacoes)

@login_required
def mudar_status(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    usuario.is_active = not usuario.is_active
    usuario.save()
    return redirect('usuario:listar_ativos')

@login_required
def mudar_status_admin(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    usuario.is_superuser = not usuario.is_superuser
    usuario.save()
    return redirect('usuario:listar_ativos')

class CadastrarUsuario(generic.CreateView):
    form_class = forms.FormCriarUsuario
    template_name = 'Usuario/cadastrar.html'
    success_url = reverse_lazy('usuario:listar_ativos')

class EditarUsuario(LoginRequiredMixin, generic.UpdateView):
    model = Usuario
    form_class = forms.FormEditarUsuario
    template_name = 'Usuario/editar.html'
    success_url = reverse_lazy('usuario:listar_ativos')

class DetalheUsuario(LoginRequiredMixin, generic.DetailView):
    model = Usuario
    template_name = "Usuario/detalhes.html"

    # usuario

class DeletarUser(LoginRequiredMixin, generic.DeleteView):
     model = Usuario
     template_name = 'Usuario/deletar.html'
     success_url = reverse_lazy('usuario:listar_ativos')

