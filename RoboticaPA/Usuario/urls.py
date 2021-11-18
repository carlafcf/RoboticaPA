from django.urls import path

from django.contrib.auth import views as auth_views
from Usuario import views

app_name = 'usuario'

urlpatterns = [
    path('cadastrar/', views.CadastrarUsuario.as_view(), name="cadastrar"),
    path('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # path('deletar/<int:pk>', views.deletar, name="deletar"),
    ##### path('detalhes/<int:pk>', views.detalhes, name="detalhes"),
    # path('editar/<int:pk>', views.editar, name="editar"),
    # path('listar/', views.listar, name="listar"),
]