from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from markupfield.fields import MarkupField
from model_utils.models import TimeStampedModel
from reversion import revisions as reversion
from taggit.managers import TaggableManager

from .querysets import ArticleQuerySet

from ..base.choices import STATUS
from ..category.models import Category


@python_2_unicode_compatible
class Article(TimeStampedModel):

    title = models.CharField(max_length=200)

    slug = models.SlugField()

    content = MarkupField(_('Content'), default_markup_type='markdown')

    category = models.ForeignKey(Category, related_name='articles')

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    status = models.IntegerField(choices=STATUS, default=STATUS.draft)

    tags = TaggableManager(blank=True)

    objects = ArticleQuerySet().as_manager()

    class Meta:
        app_label = 'django_knowledgebase'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def save(self, *args, **kwargs):
        # Newly created object, so set slug
        if not self.id:
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

reversion.register(Article)
