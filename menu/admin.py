from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'menu_type', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'menu_type')
    list_filter = ('price',)
    list_per_page = 25


admin.site.register(Menu, MenuAdmin)
