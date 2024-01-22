from django.contrib import admin
from django.db import models
from app.models.blog import Blog, Comment
from ckeditor.widgets import CKEditorWidget


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'author',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)

    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'blog', 'created_at', 'active']
    list_filter = ['active', 'created_at', 'updated_at']
    search_fields = ['name', 'email', 'body']
