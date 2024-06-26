# Generated by Django 3.2.5 on 2024-01-25 00:49

import PlanoAula.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlanoAula', '0013_auto_20240125_0047'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FotoExecução',
            new_name='FotoExecucao',
        ),
        migrations.AlterModelOptions(
            name='videorobo',
            options={'ordering': ['-plano_aula__data_criacao'], 'verbose_name': 'Vídeo do robô', 'verbose_name_plural': 'Vídeos do robô'},
        ),
        migrations.RenameField(
            model_name='videorobo',
            old_name='execucao_video',
            new_name='robo_video',
        ),
        migrations.AlterField(
            model_name='videorobo',
            name='plano_aula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='videos_robo', to='PlanoAula.planoaula', verbose_name='Plano de aula'),
        ),
        migrations.CreateModel(
            name='VideoExecucao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execucao_video', models.ImageField(blank=True, null=True, upload_to=PlanoAula.models.user_directory_path)),
                ('plano_aula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='videos_execucao', to='PlanoAula.planoaula', verbose_name='Plano de aula')),
            ],
            options={
                'verbose_name': 'Vídeo da execução',
                'verbose_name_plural': 'Vídeos da execução',
                'ordering': ['-plano_aula__data_criacao'],
            },
        ),
    ]
