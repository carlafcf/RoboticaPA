# Generated by Django 3.2.5 on 2021-12-17 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
        ('PlanoAula', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planoaula',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='Usuario.usuario'),
        ),
    ]
