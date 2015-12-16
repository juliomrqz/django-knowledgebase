#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-knowledgebase
------------

Tests for `django-knowledgebase` models module.
"""

from __future__ import absolute_import, unicode_literals

from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from django_knowledgebase.admin import ArticleAdmin
from django_knowledgebase.base.choices import STATUS
from django_knowledgebase.models import Article

from ..mommy_recipes import user, category, article


class ModifiedArticleAdmin(ArticleAdmin):

    def message_user(self, request, message):
        self.django_knowledgebase_message = message


class MockRequest(object):
    pass


class MockSuperUser(object):

    def has_perm(self, perm):
        return True


class AdminArticleTest(TestCase):

    def setUp(self):
        self.app_admin = ModifiedArticleAdmin(Article, AdminSite())
        self.request = MockRequest()
        self.request.user = MockSuperUser()

        self.user = user.make()
        self.category = category.make(
            author=self.user, _quantity=1
        )
        self.articles = article.make(
            category=self.category[0],
            author=self.user,
            _quantity=3
        )
        self.articles_published = article.make(
            category=self.category[0],
            author=self.user,
            status=STATUS.published,
            _quantity=3
        )

    def test_default_fields(self):
        defaul_fields = ['author', 'category', 'content',
                         'content_markup_type', 'slug', 'status', 'tags',
                         'title']

        fields = sorted(
            list(self.app_admin.get_form(self.request).base_fields)
        )
        self.assertEqual(fields, defaul_fields)

        fields = sorted(list(self.app_admin.get_fields(self.request)))
        self.assertEqual(fields, defaul_fields)

        fields = sorted(
            list(self.app_admin.get_fields(self.request, self.articles[0]))
        )
        self.assertEqual(fields, defaul_fields)

    def test_custom_display_fields(self):
        article = Article.objects.filter(pk=4)[0]

        self.assertEqual(
            self.app_admin.category_title(article),
            article.category.title
        )

    def test_make_draft_action(self):
        queryset = Article.objects.filter(pk=4)
        queryset_all = Article.objects.all()

        self.app_admin.make_draft(self.request, queryset)

        self.assertEqual(len(Article.objects.unpublished()), 4)
        self.assertEqual(
            self.app_admin.django_knowledgebase_message,
            '1 article was successfully marked as draft.'
        )

        self.app_admin.make_draft(self.request, queryset_all)

        self.assertEqual(len(Article.objects.unpublished()), 6)
        self.assertEqual(
            self.app_admin.django_knowledgebase_message,
            '6 articles were successfully marked as draft.'
        )

    def test_make_published_action(self):
        queryset = Article.objects.filter(pk=1)
        queryset_all = Article.objects.all()

        self.app_admin.make_published(self.request, queryset)

        self.assertEqual(len(Article.objects.published()), 4)
        self.assertEqual(
            self.app_admin.django_knowledgebase_message,
            '1 article was successfully marked as published.'
        )

        self.app_admin.make_published(self.request, queryset_all)

        self.assertEqual(len(Article.objects.published()), 6)
        self.assertEqual(
            self.app_admin.django_knowledgebase_message,
            '6 articles were successfully marked as published.'
        )

    def tearDown(self):
        pass
