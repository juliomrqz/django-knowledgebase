from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from markupfield.fields import MarkupField
from model_utils.models import TimeStampedModel

from .querysets import ArticleQuerySet

from ..base.choices import STATUS
from ..category.models import Category


@python_2_unicode_compatible
class Article(TimeStampedModel):

    title = models.CharField(max_length=200)

    category = models.ForeignKey(Category, related_name='articles')

    content = MarkupField(_('Content'), default_markup_type='markdown')

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    status = models.IntegerField(choices=STATUS, default=STATUS.draft)

    objects = ArticleQuerySet().as_manager()

    class Meta:
        app_label = 'django_knowledgebase'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.title
