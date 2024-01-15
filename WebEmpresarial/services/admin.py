from django.contrib import admin
from .models import Services
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
admin.site.register(Services,ServiceAdmin)
