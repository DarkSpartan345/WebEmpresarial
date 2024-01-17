from django.contrib import admin

from .models import Link
class LinkAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
    def get_readonly_fields(self, request, obj:None):
        if request.user.groups.filter(name="personal").exists:
            return ('created','update','key','name')
        else:
            ('created','update')
admin.site.register(Link,LinkAdmin)

