from __future__ import unicode_literals

from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by',)
    list_filter = ('modified',)
