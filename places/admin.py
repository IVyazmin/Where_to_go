from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image

admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    fields = ["image", "get_image", "number"]
    readonly_fields = ["get_image"]
    extra = 1

    def get_image(self, obj):
        if hasattr(obj.image, "url"):
            return format_html('<img src="{url}" style="max-height:200px;"/>'.format(
                url=obj.image.url
            ))
        return ""


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

