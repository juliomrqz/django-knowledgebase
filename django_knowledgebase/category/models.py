from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from markupfield.fields import MarkupField
from model_utils.models import TimeStampedModel

from .querysets import CategoryQuerySet


@python_2_unicode_compatible
class Category(TimeStampedModel):

    title = models.CharField(_('Title'), max_length=200)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    description = MarkupField(_('Description'), default_markup_type='markdown')

    objects = CategoryQuerySet().as_manager()

    class Meta:
        app_label = 'django_knowledgebase'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title
