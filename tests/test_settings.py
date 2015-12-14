from __future__ import unicode_literals

from django.test import TestCase

from django_knowledgebase.apps import DjangoKnowledgebaseConfig


class SettingsTestCase(TestCase):

    def setUp(self):
        self.AppConfig = DjangoKnowledgebaseConfig

    def test_app_config(self):
        self.assertTrue(self.AppConfig.name, 'django_knowledgebase')
        self.assertTrue(self.AppConfig.verbose_name, 'Knowledgebase')
