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

    template_name = 'knowledgebase/' + context_object_name + '.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardHomeView, self).get_context_data(**kwargs)
        context['articles_list'] = Article.objects.all()
        context['categories_list'] = Category.objects.all()

        return context


# TODO: Check Mixins Order
class DashboardArticleUpdateView(ArticleUpdateView,
                                 LoginRequiredMixin,
                                 SuperuserRequiredMixin
                                 ):
    context_object_name = 'article'
    template_name_suffix = '_dashboard_update'


class DashboardArticleDeleteView(LoginRequiredMixin,
                                 SuperuserRequiredMixin,
                                 ArticleDeleteView):
    success_url = reverse_lazy('knowledgebase:dashboard_home')
    template_name_suffix = '_dashboard_delete'


class DashboardArticleCreateView(LoginRequiredMixin,
                                 SuperuserRequiredMixin,
                                 ArticleCreateView):
    success_url = reverse_lazy('knowledgebase:dashboard_home')
    template_name_suffix = '_dashboard_create'


# TODO: Check Mixins Order
class DashboardCategoryUpdateView(CategoryUpdateView,
                                  LoginRequiredMixin,
                                  SuperuserRequiredMixin):
    template_name_suffix = '_dashboard_create'


class DashboardCategoryDeleteView(LoginRequiredMixin,
                                  SuperuserRequiredMixin,
                                  CategoryDeleteView):
    success_url = reverse_lazy('knowledgebase:dashboard_home')
    template_name_suffix = '_dashboard_delete'


class DashboardCategoryCreateView(LoginRequiredMixin,
                                  SuperuserRequiredMixin,
                                  CategoryCreateView):
    success_url = reverse_lazy('knowledgebase:dashboard_home')
    template_name_suffix = '_dashboard_create'
