# Generated by Django 3.2.5 on 2022-06-15 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Disciplina', '0004_auto_20220430_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conteudo',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='conteudos', to='Disciplina.disciplina', verbose_name='Disciplina'),
        ),
    ]
