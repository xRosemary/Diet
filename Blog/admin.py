from django.contrib import admin
from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    readonly_fields = ['date']
    fields = ['title', 'date', 'author', 'category', 'desc', 'content']
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)