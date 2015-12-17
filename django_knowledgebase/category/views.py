from django.views.generic import ListView, DetailView

from .models import Category
from ..article.models import Article


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories_list'


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context

        context = super(CategoryDetailView, self).get_context_data(**kwargs)

        # Add in a QuerySet of the Articles
        context['articles'] = Article.objects.filter(
            category=self.object
        ).all().published()

        return context
