from django.contrib.auth.models import User, AbstractUser
from django.db import models

# class Usuario(models.Model):
#     usuario = models.OneToOneField(User, on_delete=models.RESTRICT)
#     cidade = models.CharField(max_length=100, verbose_name='Cidade')
#     estado = models.CharField(max_length=100, verbose_name='Estado')

#     def __str__(self):
#         return self.usuario.first_name + " " + self.usuario.last_name

#     class Meta:
#         ordering = ['usuario']
#         verbose_name = "Usuário"
#         verbose_name_plural = "Usuários"

class Usuario(User):
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    estado = models.CharField(max_length=100, verbose_name='Estado')

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"