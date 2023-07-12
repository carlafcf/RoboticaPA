from django.shortcuts import render

def criar(request):
    return render(request, "Curso/criar.html")