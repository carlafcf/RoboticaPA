# Generated by Django 3.2.5 on 2024-01-21 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acoes', '0007_auto_20240121_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midia',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data'),
        ),
    ]
