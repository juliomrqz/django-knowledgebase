from __future__ import unicode_literals

from django.contrib import admin

from .article.admin import ArticleAdmin
from .category.admin import CategoryAdmin

from .models import Article, Category

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
