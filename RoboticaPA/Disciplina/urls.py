from django.urls import path

from Disciplina import views

app_name = 'disciplina'

urlpatterns = [
    # path('criar_disciplina/', views.CriarDisciplina.as_view(), name="criar_disciplina"),
    # path('criar_conteudo/', views.CriarConteudo.as_view(), name="criar_conteudo"),
    # path('editar_disciplina/<int:pk>/', views.EditarDisciplina.as_view(), name="editar_disciplina"),
    # path('editar_conteudo/<int:pk>/', views.EditarConteudo.as_view(), name="editar_conteudo"),
    path('listar/', views.listar, name="listar"),
    path('listar/sugerir_disciplina/', views.sugerir_disciplina, name="sugerir_disciplina"),
    path('listar/sugerir_conteudo/', views.sugerir_conteudo, name="sugerir_conteudo"),
    # path('sugerir_disciplina/', views.SugerirDisciplina.as_view(), name="sugerir_disciplina"),
    # path('sugerir_conteudo/', views.SugerirConteudo.as_view(), name="sugerir_conteudo"),
    # path('listar_sugestoes/', views.listar_sugestoes, name="listar_sugestoes"),


    # path('deletar/<int:pk>', views.Deletar.as_view(), name="deletar"),
]