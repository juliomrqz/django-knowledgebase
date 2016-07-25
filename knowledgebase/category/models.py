from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from model_utils.models import TimeStampedModel

from ..base.tools import custom_slugify

from .querysets import CategoryQuerySet


@python_2_unicode_compatible
class Category(TimeStampedModel):

    title = models.CharField(_('Title'), max_length=200)

    slug = models.SlugField(unique=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    description = models.TextField(
        _('Description'), max_length=200, blank=True
    )

    objects = CategoryQuerySet().as_manager()

    class Meta:
        app_label = 'knowledgebase'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def save(self, *args, **kwargs):
        # Newly created object, so set slug
        if not self.pk:
            if not self.slug:
                self.slug = custom_slugify(self.title)

        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'knowledgebase:category_detail', kwargs={"slug": self.slug}
        )

    def __str__(self):
        return self.title
