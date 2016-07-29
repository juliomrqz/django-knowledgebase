from django.views.generic import (CreateView, DeleteView,
                                  UpdateView, ListView)

from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
from hitcount.views import HitCountDetailView

from ..conf import settings as app_settings

from .forms import ArticleForm
from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles_list'
    queryset = model.objects.published()


class ArticleDetailView(HitCountDetailView):
    model = Article
    context_object_name = 'article'
    count_hit = app_settings['COUNT_HIT']


class ArticleUpdateView(LoginRequiredMixin,
                        SuperuserRequiredMixin,
                        UpdateView):
    model = Article
    form_class = ArticleForm
    context_object_name = 'article'


class ArticleDeleteView(LoginRequiredMixin,
                        SuperuserRequiredMixin,
                        DeleteView):
    model = Article


class ArticleCreateView(LoginRequiredMixin,
                        SuperuserRequiredMixin,
                        CreateView):
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        article = form.save(commit=False)

        article.author = self.request.user
        article.save()

        return super(ArticleCreateView, self).form_valid(form)
