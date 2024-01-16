from django.db import models

class Page(models.Model):
    name=models.CharField(verbose_name="Paginas",max_length=200)
    content=models.TextField(verbose_name="Contenido")
    update=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    class Meta:
        verbose_name="Pagina"
        verbose_name_plural=verbose_name+"s"
        ordering=["name"]
    def __str__(self):
        return self.name   