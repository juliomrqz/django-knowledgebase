# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
from slugify import slugify


def custom_slugify(value):
    return slugify(value).decode('ascii')


class CustomAutoSlugField(AutoSlugField):

    def __init__(self, *args, **kwargs):

        kwargs['populate_from'] = 'title'
        kwargs['unique'] = True
        kwargs['slugify'] = custom_slugify

        super(CustomAutoSlugField, self).__init__(*args, **kwargs)
