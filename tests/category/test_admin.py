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

from django_knowledgebase.admin import CategoryAdmin
from django_knowledgebase.models import Category

from ..mommy_recipes import user, category


class MockRequest(object):
    pass


class MockSuperUser(object):

    def has_perm(self, perm):
        return True

request = MockRequest()
request.user = MockSuperUser()


class AdminCategoryTest(TestCase):

    def setUp(self):
        self.admin = CategoryAdmin(Category, AdminSite())
        self.user = user.make()
        self.category = category.make(
            author=self.user, _quantity=1
        )

    def test_default_fields(self):
        self.assertEqual(
            list(self.admin.get_form(request).base_fields),
            ['title', 'slug', 'author', 'description']
        )

        self.assertEqual(
            list(self.admin.get_fields(request)),
            ['title', 'slug', 'author', 'description']
        )

        self.assertEqual(
            list(self.admin.get_fields(request, self.category[0])),
            ['title', 'slug', 'author', 'description']
        )

    def tearDown(self):
        pass
