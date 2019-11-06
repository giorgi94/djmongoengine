from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    alias = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class Article(models.Model):
    title = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )

    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name = _("article")
        verbose_name_plural = _("articles")
