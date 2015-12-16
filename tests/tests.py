#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-knowledgebase
------------

Tests for `django-knowledgebase` models module.
"""

from __future__ import absolute_import, unicode_literals

from django.test import TestCase

from django_knowledgebase.base.choices import STATUS
from .mommy_recipes import user, category, article


class ArticleCategorySetUpMixin(TestCase):

    def setUp(self):
        self.user_one = user.make()
        self.user_two = user.make()

        self.categories = category.make(author=self.user_one)
        self.categories_user_two = category.make(
            author=self.user_two, _quantity=5
        )

        self.articles_one = article.make(
            category=self.categories[0],
            author=self.user_one,

        )
        self.articles_two = article.make(
            category=self.categories[1],
            author=self.user_one,
            status=STATUS.published,

        )
        self.articles_three = article.make(
            category=self.categories[2],
            author=self.user_one,
        )

        self.articles_user_two = article.make(
            category=self.categories[0],
            author=self.user_two,
            _quantity=3
        )

        self.custom_article = article.make(
            title="Custom Article",
            category=self.categories[0],
            author=self.user_two,
            status=STATUS.published,
            content="# Title",
            _quantity=1
        )

        # Add tags
        for art in self.articles_one:
            art.tags.add("red", "green", "blue")

        self.articles_one[1].tags.add("yellow")

        self.custom_article[0].tags.add("red")
