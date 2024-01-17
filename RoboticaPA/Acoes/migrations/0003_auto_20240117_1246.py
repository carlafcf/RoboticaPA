# Generated by Django 3.2.5 on 2024-01-17 12:46

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Acoes', '0002_alter_acoes_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acoes',
            name='data_inicio',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de início'),
        ),
        migrations.AlterField(
            model_name='mensagemacoes',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
    ]