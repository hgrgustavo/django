# Generated by Django 5.1.3 on 2024-11-07 00:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('capa', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('editora', models.CharField(max_length=100)),
                ('ano_public', models.DateField(verbose_name='Ano de publicacao')),
                ('colecao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuslivros.colecao')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=100)),
                ('texto', models.TextField(max_length=255)),
                ('livro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuslivros.livro')),
            ],
        ),
        migrations.AddField(
            model_name='colecao',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuslivros.usuario'),
        ),
    ]