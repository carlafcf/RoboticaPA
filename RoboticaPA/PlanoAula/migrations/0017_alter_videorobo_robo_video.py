# Generated by Django 3.2.5 on 2024-01-29 20:21

import PlanoAula.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanoAula', '0016_auto_20240129_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videorobo',
            name='robo_video',
            field=models.FileField(blank=True, null=True, upload_to=PlanoAula.models.diretorio_plano_aula_midias, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mpeg', 'wmv'])], verbose_name='Vídeos do robô'),
        ),
    ]