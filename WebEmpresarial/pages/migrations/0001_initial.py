# Generated by Django 5.0.1 on 2024-01-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Paginas')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Paginas',
                'ordering': ['name'],
            },
        ),
    ]
