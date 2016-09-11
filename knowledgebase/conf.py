# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import collections

from django.conf import settings as _settings
from django.core.signals import setting_changed
from django.dispatch import receiver


DEFAULTS = {
    'COUNT_HIT': True,
}


class KnowledgebaseSettings(collections.MutableMapping):
    """
    Container object for Knowledgebase settings
    """

    def __init__(self, wrapped_settings):
        self.settings = DEFAULTS.copy()
        self.settings.update(wrapped_settings)

    def __getitem__(self, key):
        return self.settings[key]

    def __setitem__(self, key, value):
        self.settings[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.settings)

    def __len__(self):
        return len(self.settings)

    def __getattr__(self, name):
        return self.__getitem__(name)


_settings_KNOWLEDGEBASE = []
if hasattr(_settings, "KNOWLEDGEBASE"):
    _settings_KNOWLEDGEBASE = _settings.KNOWLEDGEBASE

settings = KnowledgebaseSettings(_settings_KNOWLEDGEBASE)


@receiver(setting_changed)
def reload_settings(**kwargs):
    if kwargs['setting'] == 'KNOWLEDGEBASE':
        settings.update(kwargs['value'])
