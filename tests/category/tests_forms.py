from __future__ import unicode_literals

from django.test import TestCase

from knowledgebase.forms import CategoryForm


class CategoryFormTestCase(TestCase):

    def test_with_empty_data_should_fail(self):
        form = CategoryForm({})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['title'], ['This field is required.'])

    def test_form_initial_value(self):
        form = CategoryForm()

        self.assertEqual(form.fields['slug'].initial, None)
