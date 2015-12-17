from __future__ import unicode_literals

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(
        regex=r"^$",
        view=views.CategoryListView.as_view(),
        name="category_list"
    ),
    url(
        regex=r"^(?P<slug>[\w-]+)/$",
        view=views.CategoryDetailView.as_view(),
        name="category_detail"
    )
)
