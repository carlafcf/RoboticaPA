from django.db import models
from datetime import date
from django.utils import timezone

from Usuario.models import Usuario

TIPO = [
    ('Evento', 'Evento'),
    ('Curso', 'Curso'),
    ('Palestra', 'Palestra')
]

def user_directory_path(instance, filename):
    return 'user_{0}/acao_{1}/{2}'.format(instance.acao.responsavel.id, instance.acao.id, filename)


class Acoes(models.Model):
    titulo = models.CharField(max_length=500, verbose_name="Título")
    tipo = models.CharField(max_length=8, choices=TIPO, default='Evento')
    data_inicio = models.DateField(default = date.today, verbose_name = "Data de início")
    data_fim = models.DateField(null=True, blank = True, verbose_name = "Data de fim")
    local = models.CharField(max_length=200, null=True, blank=True, verbose_name="Local")
    descricao = models.TextField(null=True, blank=True,verbose_name="Descrição")
    responsavel = models.ForeignKey(Usuario, on_delete=models.RESTRICT,verbose_name="Responsável")

    def __str__(self):
        return str(self.tipo) + " - " + str(self.titulo)

    class Meta:
        ordering = ['-data_inicio', 'titulo']
        verbose_name = "Ação"
        verbose_name_plural = "Ações"

class Midia(models.Model):
    acao = models.ForeignKey(Acoes, on_delete=models.RESTRICT,verbose_name="Ação")
    midia = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return str(self.acao)

    class Meta:
        ordering = ['acao']
        verbose_name = "Mídia"
        verbose_name_plural = "Mídias"

class MensagemAcoes(models.Model):
    texto = models.TextField(verbose_name="Texto")
    data = models.DateTimeField(default = timezone.now, verbose_name = "Data")
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT,verbose_name="Usuário")
    acao = models.ForeignKey(Acoes, on_delete=models.RESTRICT,verbose_name="Ação")
    mensagem_original = models.ForeignKey('self', null=True, blank = True, on_delete=models.RESTRICT,verbose_name="Mensagem original")

    def __str__(self):
        return str(self.acao) + " - " + str(self.data)

    class Meta:
        ordering = ['acao', '-data']
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"