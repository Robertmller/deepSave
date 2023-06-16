from django.contrib import admin
from core.models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ["name", "title"]

    @admin.display(ordering="name")
    def link_name(self, obj):
        return obj.link.name


admin.site.register(Link, LinkAdmin)
