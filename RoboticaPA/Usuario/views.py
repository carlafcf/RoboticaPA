from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

from Usuario import forms
from Usuario.models import Usuario
from Disciplina.models import Disciplina

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

class Cadastrar(generic.CreateView):
    form_class = forms.FormCriarUsuario
    template_name = 'Usuario/cadastrar.html'
    success_url = reverse_lazy('usuario:login')

def completar_cadastro(request, pk):

    disciplinas = Disciplina.objects.filter(status='Ativo')

    if (request.method == "POST"):
        form_usuario = forms.FormCompletarCadastro(request.POST)
        if (form_usuario.is_valid()):
            usuario = Usuario.objects.get(pk=pk)
            usuario.first_name = form_usuario.cleaned_data['first_name']
            usuario.last_name = form_usuario.cleaned_data['last_name']
            usuario.cidade = form_usuario.cleaned_data['cidade']
            usuario.estado = form_usuario.cleaned_data['estado']
            usuario.save()
    else:
        form_usuario = forms.FormCompletarCadastro()
        form_interesses = forms.FormAtualizarInteresses()
    
    informacoes = {
        'form_usuario': form_usuario,
        'form_interesses': form_interesses,
        'disciplinas': disciplinas
    }
    return render(request, "usuario/completar_cadastro.html", informacoes)

class CompletarCadastro(LoginRequiredMixin, generic.UpdateView):
    model = Usuario
    form_class = forms.FormCompletarCadastro
    template_name = 'Usuario/completar_cadastro.html'
    success_url = reverse_lazy('home')

class Editar(LoginRequiredMixin, generic.UpdateView):
    model = Usuario
    form_class = forms.FormEditarUsuario
    template_name = 'Usuario/editar.html'

    def get_success_url(self):
           pk = self.kwargs["pk"]
           return reverse_lazy("usuario:editar", kwargs={"pk": pk})

def alterar_avatar(request, pk, novo):
    if (novo == 0):
        usuario = Usuario.objects.get(pk=pk)
        usuario.avatar = 'profile-pic/default.jpeg'
        usuario.save()
        return redirect('usuario:editar', pk=pk)
    else:
        pass

class AlterarSenha(LoginRequiredMixin, generic.UpdateView):
    model = Usuario
    form_class = forms.FormEditarSenha
    template_name = 'Usuario/alterar_senha.html'

    def get_success_url(self):
           pk = self.kwargs["pk"]
           return reverse_lazy("usuario:editar", kwargs={"pk": pk})

class Detalhes(LoginRequiredMixin, generic.DetailView):
    model = Usuario
    template_name = "Usuario/detalhes.html"
    # usuario
    # object

class DeletarUser(LoginRequiredMixin, generic.DeleteView):
     model = Usuario
     template_name = 'Usuario/deletar.html'
     success_url = reverse_lazy('usuario:listar_ativos')

