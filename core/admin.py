from django.contrib import admin
from core.models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "image",
                    "category", "description", "isLinkOnline"]

    @admin.display(ordering="title")
    def link_url(self, obj):
        return obj.link.link

    def link_title(self, obj):
        return obj.link.title


admin.site.register(Link, LinkAdmin)
