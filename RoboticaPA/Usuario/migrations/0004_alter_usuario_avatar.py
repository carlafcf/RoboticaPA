# Generated by Django 3.2.5 on 2022-01-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0003_alter_usuario_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(default='profile-pic/default.jpeg', upload_to='profile-pic/'),
        ),
    ]
