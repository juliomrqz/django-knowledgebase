from __future__ import unicode_literals

from django.test import TestCase

from knowledgebase.base.choices import STATUS
from knowledgebase.forms import ArticleForm


class ArticleFormTestCase(TestCase):

    def test_with_empty_data_should_fail(self):
        form = ArticleForm({})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
        self.assertEqual(form.errors['title'], ['This field is required.'])
        self.assertEqual(form.errors['content'], ['This field is required.'])
        self.assertEqual(form.errors['category'], ['This field is required.'])
        self.assertEqual(form.errors['status'], ['This field is required.'])

    def test_form_initial_value(self):
        form = ArticleForm()

        self.assertEqual(form.fields['status'].initial, STATUS.draft)
        self.assertEqual(form.fields['slug'].initial, None)
