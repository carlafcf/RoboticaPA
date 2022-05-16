from django.db import models
from django.utils import timezone

from Usuario.models import Usuario
from Disciplina.models import Conteudo

class PlanoAula(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    contextualizacao = models.TextField(verbose_name="Contextualização")
    descricao_atividade = models.TextField(verbose_name="Descrição da atividade")
    responsavel = models.ForeignKey(Usuario, on_delete=models.RESTRICT,null=True, verbose_name="Responsável")
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="Data de criação")
    conteudos = models.ManyToManyField(Conteudo, verbose_name="Conteúdos")
    # robo_tipo = 
    # robo_descricao = 
    # robo_fotos

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']
        verbose_name = "Plano de aula"
        verbose_name_plural = "Planos de aula"

