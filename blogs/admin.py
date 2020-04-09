from django.contrib import admin
from .models import Blogs


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_writter', 'blog_type')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'blog_writter', 'blog_type')
    list_filter = ('blog_date',)
    list_per_page = 20


admin.site.register(Blogs, BlogsAdmin)
