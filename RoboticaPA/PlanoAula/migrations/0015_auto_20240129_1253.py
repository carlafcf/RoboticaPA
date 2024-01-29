# Generated by Django 3.2.5 on 2024-01-29 12:53

import PlanoAula.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanoAula', '0014_auto_20240125_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotoexecucao',
            name='execucao_foto',
            field=models.ImageField(blank=True, null=True, upload_to=PlanoAula.models.diretorio_plano_aula_midias, verbose_name='Fotos da execução da atividade'),
        ),
        migrations.AlterField(
            model_name='fotorobo',
            name='robo_foto',
            field=models.ImageField(blank=True, null=True, upload_to=PlanoAula.models.diretorio_plano_aula_midias, verbose_name='Fotos do robô'),
        ),
        migrations.AlterField(
            model_name='planoaula',
            name='prog_codigos',
            field=models.FileField(blank=True, null=True, upload_to=PlanoAula.models.diretorio_plano_aula, verbose_name='Códigos'),
        ),
        migrations.AlterField(
            model_name='planoaula',
            name='robo_pdf',
            field=models.FileField(blank=True, null=True, upload_to=PlanoAula.models.diretorio_plano_aula, verbose_name='Manual de montagem do robô'),
        ),
        migrations.AlterField(
            model_name='videoexecucao',
            name='execucao_video',
            field=models.ImageField(blank=True, null=True, upload_to=PlanoAula.models.diretorio_plano_aula_midias, verbose_name='Vídeos da execução da atividade'),
        ),
        migrations.AlterField(
            model_name='videorobo',
            name='robo_video',
            field=models.ImageField(blank=True, null=True, upload_to=PlanoAula.models.diretorio_plano_aula_midias, verbose_name='Vídeos do robô'),
        ),
    ]
