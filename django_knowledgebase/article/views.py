from django.views.generic import (CreateView, DeleteView, DetailView,
                                  UpdateView, ListView)
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin

from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles_list'
    queryset = model.objects.published()


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'


class ArticleUpdateView(LoginRequiredMixin,
                        SuperuserRequiredMixin,
                        UpdateView):
    model = Article
    fields = ['title', 'slug', 'content', 'category', 'status', 'tags']

    context_object_name = 'article'


class ArticleDeleteView(DeleteView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'slug', 'content', 'category', 'status', 'tags']
