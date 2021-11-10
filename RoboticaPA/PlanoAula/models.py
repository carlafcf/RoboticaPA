from django.db import models

# from Usuario.models import Usuario

class PlanoAula(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    contextualizacao = models.TextField(verbose_name="Contextualização")
    descricao_atividade = models.TextField(verbose_name="Descrição da atividade")
    # usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    # robo_tipo = 
    # robo_descricao = 
    # robo_fotos

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']

