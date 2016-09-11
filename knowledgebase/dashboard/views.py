from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

from ..article.models import Article
from ..article.views import (ArticleCreateView, ArticleDeleteView,
                             ArticleUpdateView)
from ..category.models import Category
from ..category.views import (CategoryCreateView, CategoryDeleteView,
                              CategoryUpdateView)


class DashboardHomeView(LoginRequiredMixin,
                        SuperuserRequiredMixin,
                        TemplateView):
    context_object_name = 'dashboard_home'

    template_name = 'knowledgebase/dashboard_home.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardHomeView, self).get_context_data(**kwargs)

        articles_list = Article.objects.all()
        articles_list = articles_list.prefetch_related("author")
        articles_list = articles_list.prefetch_related("category")
        context['articles_list'] = articles_list

        categories_list = Category.objects.all()
        categories_list = categories_list.prefetch_related("author")
        context['categories_list'] = categories_list

        return context


class DashboardArticleUpdateView(ArticleUpdateView):
    template_name_suffix = '_dashboard_update'


class DashboardArticleDeleteView(ArticleDeleteView):
    success_url = reverse_lazy('knowledgebase:dashboard_home')
    template_name_suffix = '_dashboard_delete'


class DashboardArticleCreateView(ArticleCreateView):
    success_url = reverse_lazy('knowledgebase:dashboard_home')
    template_name_suffix = '_dashboard_create'


class DashboardCategoryUpdateView(CategoryUpdateView):
    template_name_suffix = '_dashboard_update'


class DashboardCategoryDeleteView(CategoryDeleteView):
    success_url = reverse_lazy('knowledgebase:dashboard_home')
    template_name_suffix = '_dashboard_delete'


class DashboardCategoryCreateView(CategoryCreateView):
    success_url = reverse_lazy('knowledgebase:dashboard_home')
    template_name_suffix = '_dashboard_create'
