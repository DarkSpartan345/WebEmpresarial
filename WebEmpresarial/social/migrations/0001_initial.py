# Generated by Django 5.0.1 on 2024-01-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.SlugField(max_length=100, unique=True, verbose_name='nombre clave')),
                ('name', models.CharField(max_length=200, verbose_name='red social')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Enlace',
                'verbose_name_plural': 'Enlaces',
                'ordering': ['name'],
            },
        ),
    ]
