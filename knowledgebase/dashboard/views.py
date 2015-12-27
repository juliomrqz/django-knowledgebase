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
        context['articles_list'] = Article.objects.all()
        context['categories_list'] = Category.objects.all()

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
