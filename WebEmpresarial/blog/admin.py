from django.contrib import admin
from .models import Post,Category
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
    list_display=('title','author','published','post_categories')
    ordering=('author','published')
    search_fields=('title','author__username','content','Categories__name')
    date_hierarchy='published'
    list_filter=('author__username','Categories__name')
    
    def post_categories(self,obj):
        return ",".join([c.name for c in obj.Categories.all().order_by("name")])
    post_categories.short_description='Categorias'
class CategoriesAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoriesAdmin)
