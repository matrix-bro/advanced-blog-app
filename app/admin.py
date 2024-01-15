from django.contrib import admin

from app.models.blog import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'author',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
