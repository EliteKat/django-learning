from django.contrib import admin
from .models import PBoard


class Admin_PBoard(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(PBoard, Admin_PBoard)
