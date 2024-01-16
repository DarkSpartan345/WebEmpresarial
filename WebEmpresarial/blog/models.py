from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name="Categoria")
    update=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering=["-created"]
    def __str__(self):
        return self.name
class Post(models.Model):
    title=models.CharField(max_length=200,verbose_name="Titulo")
    content=models.TextField(verbose_name="contenido")
    published=models.DateTimeField(verbose_name="Fecha de publicacion",default=now)
    image=models.ImageField(verbose_name="Imagen",upload_to="Blog",null=True,blank=True)
    author=models.ForeignKey(User,verbose_name="Autor",on_delete=models.CASCADE)
    Categories=models.ManyToManyField(Category,verbose_name="Categorias", related_name="get_post")
    update=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    class Meta:
        verbose_name="Entrada"
        verbose_name_plural="Entradas"
        ordering=["-created"]
    def __str__(self):
        return self.title    
    
