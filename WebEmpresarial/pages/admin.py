from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
admin.site.register(Page,PageAdmin)
