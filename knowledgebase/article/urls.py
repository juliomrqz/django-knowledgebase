from __future__ import unicode_literals

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(
        regex=r"^$",
        view=views.ArticleListView.as_view(),
        name="article_list"
    ),
    url(
        regex=r"^(?P<slug>[\w-]+)/*$",
        view=views.ArticleDetailView.as_view(),
        name="article_detail"
    ),
)
