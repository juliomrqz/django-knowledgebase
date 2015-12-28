from __future__ import unicode_literals

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(
        regex=r"^$",
        view=views.DashboardHomeView.as_view(),
        name="dashboard_home"
    ),
    url(
        regex=r"^article/(?P<pk>\d+)/$",
        view=views.DashboardArticleUpdateView.as_view(),
        name="dashboard_article_update"
    ),
    url(
        regex=r"^article/delete/(?P<pk>\d+)/$",
        view=views.DashboardArticleDeleteView.as_view(),
        name="dashboard_article_delete"
    ),
    url(
        regex=r"^article/create/$",
        view=views.DashboardArticleCreateView.as_view(),
        name="dashboard_article_create"
    ),
    url(
        regex=r"^category/(?P<pk>\d+)/$",
        view=views.DashboardCategoryUpdateView.as_view(),
        name="dashboard_category_update"
    ),
    url(
        regex=r"^category/delete/(?P<pk>\d+)/$",
        view=views.DashboardCategoryDeleteView.as_view(),
        name="dashboard_category_delete"
    ),
    url(
        regex=r"^category/create/$",
        view=views.DashboardCategoryCreateView.as_view(),
        name="dashboard_category_create"
    )
)
