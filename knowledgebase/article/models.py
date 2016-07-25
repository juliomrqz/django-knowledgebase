from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from django_markup.fields import MarkupField
from model_utils.models import TimeStampedModel
from reversion import revisions as reversion
from taggit.managers import TaggableManager

from ..base.choices import STATUS
from ..base.tools import custom_slugify
from ..category.models import Category

from .querysets import ArticleQuerySet


@python_2_unicode_compatible
class Article(TimeStampedModel):

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    content = models.TextField(_('Content'))

    markup = MarkupField(default='markdown')

    category = models.ForeignKey(Category, related_name='articles')

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    status = models.IntegerField(choices=STATUS, default=STATUS.draft)

    tags = TaggableManager(blank=True)

    objects = ArticleQuerySet().as_manager()

    class Meta:
        app_label = 'knowledgebase'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def save(self, *args, **kwargs):
        # Newly created object, so set slug
        if not self.pk:
            if not self.slug:
                self.slug = custom_slugify(self.title)

        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'knowledgebase:article_detail', kwargs={"slug": self.slug}
        )

    def __str__(self):
        return self.title

reversion.register(Article)
