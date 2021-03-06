# Generated by Django 3.2.5 on 2022-03-10 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuario', '0004_alter_usuario_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='SugestaoDisciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('status', models.CharField(choices=[('A', 'Em espera'), ('B', 'Aprovado'), ('C', 'Negado')], default='A', max_length=1)),
                ('comentarios', models.TextField(blank=True, null=True, verbose_name='Comentários')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='Usuario.usuario', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Sugestão de Disciplina',
                'verbose_name_plural': 'Sugestões de Disciplina',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='SugestaoConteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('status', models.CharField(choices=[('A', 'Em espera'), ('B', 'Aprovado'), ('C', 'Negado')], default='A', max_length=1)),
                ('comentarios', models.TextField(blank=True, null=True, verbose_name='Comentários')),
                ('disciplina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='Disciplina.disciplina', verbose_name='Disciplina')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='Usuario.usuario', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Sugestão de Conteúdo',
                'verbose_name_plural': 'Sugestões de Conteúdo',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Conteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('disciplina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='Disciplina.disciplina', verbose_name='Disciplina')),
            ],
            options={
                'verbose_name': 'Conteúdo',
                'verbose_name_plural': 'Conteúdos',
                'ordering': ['nome'],
            },
        ),
    ]
