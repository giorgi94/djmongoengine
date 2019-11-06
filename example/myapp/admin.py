from django.contrib import admin

from .models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("alias",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ("alias",)
