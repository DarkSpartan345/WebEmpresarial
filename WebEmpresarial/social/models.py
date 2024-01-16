from django.db import models

class Link(models.Model):
    key=models.SlugField(verbose_name="nombre clave",max_length=100,unique=True)
    name=models.CharField(verbose_name="red social",max_length=200)
    url=models.URLField(verbose_name="Enlace",max_length=200,null=True,blank=True)
    update=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    class Meta:
        verbose_name="Enlace"
        verbose_name_plural="Enlaces"
        ordering=["name"]
    def __str__(self):
        return self.name       
