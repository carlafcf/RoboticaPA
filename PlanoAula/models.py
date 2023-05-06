from django.db import models
from django.utils import timezone

from Usuario.models import Usuario
from Disciplina.models import Conteudo

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/plano_aula_<id>/<filename>
    return 'user_{0}/plano_aula_{1}/{2}'.format(instance.responsavel.id, instance.data_criacao, filename)

class PlanoAula(models.Model):

    responsavel = models.ForeignKey(Usuario, on_delete=models.RESTRICT,null=True, verbose_name="Responsável")
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="Data de criação")

    # Gerais
    titulo = models.CharField(max_length=200, verbose_name="Título")
    contextualizacao = models.TextField(verbose_name="Contextualização")
    descricao_atividade = models.TextField(verbose_name="Descrição da atividade")
    avaliacao = models.TextField(verbose_name="Critérios de avaliação", default="", blank=True, null=True)
    conteudos = models.ManyToManyField(Conteudo, related_name="planos_de_aula", verbose_name="Conteúdos")

    # Montagem
    robo_equipamento = models.CharField(max_length=200, verbose_name="Equipamento", default="")
    robo_descricao = models.TextField(verbose_name="Descrição do robô", default="")
    robo_link = models.TextField(verbose_name="Links", blank=True, null=True)

    # Programação
    prog_linguagem = models.CharField(max_length=200, verbose_name="Linguagem de programação", default="")
    prog_descricao = models.TextField(verbose_name="Descrição da programação", default="")
    prog_link = models.TextField(verbose_name="Links", blank=True, null=True)
    prog_codigos = models.FileField(upload_to=user_directory_path, blank=True, null=True, verbose_name="Códigos")

    # Mídias
    robo_fotos = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    robo_videos = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    robo_pdf = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    exec_fotos = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    exec_videos = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']
        verbose_name = "Plano de aula"
        verbose_name_plural = "Planos de aula"

class LikePlanoAula(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT,null=True, verbose_name="Usuário")
    plano_aula = models.ForeignKey(PlanoAula, related_name='likes', on_delete=models.RESTRICT,null=True, verbose_name="Plano de aula")

    class Meta:
        ordering = ['usuario']
        verbose_name = "Like"
        verbose_name_plural = "Likes"

class ExecucaoPlanoAula(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT,null=True, verbose_name="Usuário")
    plano_aula = models.ForeignKey(PlanoAula, related_name='execucoes', on_delete=models.RESTRICT,null=True, verbose_name="Plano de aula")

    class Meta:
        ordering = ['usuario']
        verbose_name = "Execução"
        verbose_name_plural = "Execuções"