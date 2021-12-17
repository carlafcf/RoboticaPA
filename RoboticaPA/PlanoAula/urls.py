from django.urls import path

from PlanoAula import views

app_name = 'plano_aula'

urlpatterns = [
    path('criar/', views.Criar.as_view(), name="criar"),
    # path('deletar/<int:pk>', views.deletar, name="deletar"),
    ##### path('detalhes/<int:pk>', views.detalhes, name="detalhes"),
    path('editar/<int:pk>', views.editar, name="editar"),
    path('listar/', views.listar, name="listar"),
]