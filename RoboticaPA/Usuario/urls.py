from django.urls import path

from django.contrib.auth import views as auth_views
from Usuario import views

app_name = 'usuario'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('cadastrar/', views.CadastrarUsuario.as_view(), name="cadastrar"),
    path('editar/<int:pk>', views.EditarUsuario.as_view(), name = 'editar'),
    path('listar_ativos/', views.listar_ativos, name='listar_ativos'),
    path('listar_inativos/', views.listar_inativos, name='listar_inativos'),
    path('detalhes/<int:pk>', views.DetalheUsuario.as_view(), name='detalhes'),
    path('mudar_status/<int:pk>', views.mudar_status, name='mudar_status'),
    path('mudar_status_admin/<int:pk>', views.mudar_status_admin, name='mudar_status_admin'),
    path('deletarUsuario/<int:pk>', views.DeletarUser.as_view(), name='deletar'),
]