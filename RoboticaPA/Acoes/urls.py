from django.urls import path

from Acoes import views

app_name = 'acoes'

urlpatterns = [
    path('criar/', views.CriarAcao.as_view(), name='criar'),
    path('deletar/<int:pk>/', views.deletar, name='deletar'),
    # path('detalhes/<int:pk>/', views.Detalhe.as_view(), name='detalhes'),
    path('editar/<int:pk>/', views.EditarAcao.as_view(), name='editar'),
    path('listar/<int:pk>', views.ListarAcoesUsuario.as_view(), name='listar_usuario'),
    path('listar/', views.ListarTodasAcoes.as_view(), name='listar'),
]