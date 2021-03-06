from __future__ import unicode_literals

from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('title', 'author',)
    list_filter = ('modified',)
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ('author',)
