from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles_list'
    queryset = model.objects.published()


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
