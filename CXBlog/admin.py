from django.contrib import admin
from .models import Post, Comment
from django.contrib import admin
from .forms import BlogForm
from pagedown.widgets import AdminPagedownWidget
from django import forms

class PostAdmin(admin.ModelAdmin):
    form = BlogForm
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
    # form = BlogForm
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)




