from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin

from .models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("preview", "title", "is_active", "order")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("title",)
    ordering = ("order",)

    def preview(self, obj: SliderImage):
        if not obj.image_id:
            return "—"
        try:
            url = obj.image.url
        except Exception:
            return "—"
        return format_html(
            '<img src="{}" style="height:50px;width:auto;border-radius:6px;" />',
            url,
        )

    preview.short_description = "Превью"