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


class ArticleDeleteView(LoginRequiredMixin,
                        SuperuserRequiredMixin,
                        DeleteView):
    model = Article


class ArticleCreateView(LoginRequiredMixin,
                        SuperuserRequiredMixin,
                        CreateView):
    model = Article
    fields = ['title', 'slug', 'content', 'category', 'status', 'tags']

    def form_valid(self, form):
        article = form.save(commit=False)

        article.author = self.request.user
        article.save()

        return super(ArticleCreateView, self).form_valid(form)
