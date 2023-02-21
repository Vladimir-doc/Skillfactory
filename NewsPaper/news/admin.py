from django.contrib import admin
from .models import Category, Post, PostCategory

class PostCategoryInLine(admin.TabularInline):
    model = PostCategory
    fk_name = 'postThrough'
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInLine]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
