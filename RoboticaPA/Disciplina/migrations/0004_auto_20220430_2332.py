# Generated by Django 3.2.5 on 2022-04-30 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disciplina', '0003_alter_conteudo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='conteudo',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], default='Ativo', max_length=7),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], default='Ativo', max_length=7),
        ),
    ]
