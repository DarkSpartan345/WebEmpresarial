# Generated by Django 5.0.1 on 2024-01-15 16:22

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Categoria')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='contenido')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicacion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Blog', verbose_name='Imagen')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('Categories', models.ManyToManyField(to='blog.category', verbose_name='Categorias')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'ordering': ['-created'],
            },
        ),
    ]
