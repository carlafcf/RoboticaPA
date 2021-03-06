from django.urls import path

from PlanoAula import views

#from .views import deletar

app_name = 'plano_aula'

urlpatterns = [
    path('criar/', views.Criar.as_view(), name="criar"),

    path('deletar/<int:pk>', views.Deletar.as_view(), name="deletar"),
   ## path('detalhes/<int:pk>', views.Detalhe.as_view(), name='detalhes'),
    path('editar/<int:pk>/', views.Editar.as_view(), name="editar"),
    path('listar/<int:pk>', views.listar_usuario, name="listar_usuario"),

]