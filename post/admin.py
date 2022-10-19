from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'iconname')
    list_display_links = ('id', 'name')
    filter = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'category', 'sees', 'created', 'updated')
    list_display_links = ('id', 'user', 'title', 'category',)
    filter = ('user', 'category',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created',)
    list_display_links = ('id', 'user', 'post', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)