from django.contrib import admin
from .models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "content")
    search_fields = ("title", "text",)
    list_filter = ("time_create", "time_update")


admin.site.register(Category)