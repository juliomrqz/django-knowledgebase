from __future__ import unicode_literals

from django.test import TestCase

from knowledgebase.apps import DjangoKnowledgebaseConfig


class SettingsTestCase(TestCase):

    def setUp(self):
        self.AppConfig = DjangoKnowledgebaseConfig

    def test_app_config(self):
        self.assertTrue(self.AppConfig.name, 'knowledgebase')
        self.assertTrue(self.AppConfig.verbose_name, 'Knowledgebase')
