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
            created_by=self.user, _quantity=1
        )
        self.articles = article.make(
            category=self.category[0],
            created_by=self.user,
            _quantity=3
        )
        self.articles_published = article.make(
            category=self.category[0],
            created_by=self.user,
            status=STATUS.published,
            _quantity=3
        )

    def test_default_fields(self):
        defaul_fields = ['category', 'content', 'content_markup_type',
                         'created_by', 'slug', 'status', 'tags', 'title']

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

        self.assertEqual(self.app_admin.votes(article), 0)
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

    def test_upvote_action(self):
        queryset = Article.objects.filter(pk=1)
        queryset_all = Article.objects.all()

        self.app_admin.upvote(self.request, queryset)

        total_upvotes = 0
        for article_obj in Article.objects.all():
            total_upvotes += article_obj.total_upvotes

        self.assertEqual(total_upvotes, 1)
        self.assertEqual(
            self.app_admin.django_knowledgebase_message,
            '1 article was successfully upvoted.'
        )

        self.app_admin.upvote(self.request, queryset_all)

        total_upvotes = 0
        for article_obj in Article.objects.all():
            total_upvotes += article_obj.total_upvotes

        self.assertEqual(total_upvotes, 7)
        self.assertEqual(
            self.app_admin.django_knowledgebase_message,
            '6 articles were successfully upvoted.'
        )

    def test_downvote_action(self):
        queryset = Article.objects.filter(pk=2)
        queryset_all = Article.objects.all()

        self.app_admin.downvote(self.request, queryset)

        total_downvotes = 0
        for article_obj in Article.objects.all():
            total_downvotes += article_obj.total_downvotes

        self.assertEqual(total_downvotes, 1)
        self.assertEqual(
            self.app_admin.django_knowledgebase_message,
            '1 article was successfully downvoted.'
        )

        self.app_admin.downvote(self.request, queryset_all)

        total_downvotes = 0
        for article_obj in Article.objects.all():
            total_downvotes += article_obj.total_downvotes

        self.assertEqual(total_downvotes, 7)
        self.assertEqual(
            self.app_admin.django_knowledgebase_message,
            '6 articles were successfully downvoted.'
        )

    def tearDown(self):
        pass
