from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from .article import urls as article_urls
from .category import urls as category_urls
from .dashboard import urls as dashboard_urls

urlpatterns = patterns(
    '',

    url(r'^article/', include(article_urls)),

    url(r'^category/', include(category_urls)),

    url(r'^search/', include('haystack.urls')),

    url(r'^dashboard/', include(dashboard_urls)),
)
