from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase

from .models import Place, Image

admin.site.register(Image)


class ImageInline(SortableStackedInline):
    model = Image
    fields = ["image", "preview", "number"]
    readonly_fields = ["preview"]
    extra = 1

    def preview(self, obj):
        if hasattr(obj.image, "url"):
            return format_html('<img src="{url}" style="max-height:200px;"/>'.format(
                url=obj.image.url
            ))
        return ""


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]

