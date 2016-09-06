from django.views.generic import (CreateView, DeleteView,
                                  UpdateView, ListView)
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from braces.views import (AjaxResponseMixin, JSONResponseMixin,
                          LoginRequiredMixin, MessageMixin,
                          SuperuserRequiredMixin)
from hitcount.views import HitCountDetailView

from ..conf import settings as app_settings

from .forms import ArticleForm
from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles_list"
    queryset = model.objects.published()


class ArticleDetailView(HitCountDetailView):
    model = Article
    context_object_name = "article"
    count_hit = app_settings['COUNT_HIT']


class ArticleUpdateView(LoginRequiredMixin,
                        SuperuserRequiredMixin,
                        UpdateView):
    model = Article
    form_class = ArticleForm
    context_object_name = "article"


class ArticleDeleteView(LoginRequiredMixin,
                        SuperuserRequiredMixin,
                        DeleteView):
    model = Article


class ArticleCreateView(LoginRequiredMixin,
                        SuperuserRequiredMixin,
                        CreateView):
    model = Article
    context_object_name = "article"
    form_class = ArticleForm

    def form_valid(self, form):
        article = form.save(commit=False)

        article.author = self.request.user
        article.save()

        return super(ArticleCreateView, self).form_valid(form)


class ArticleVoteView(MessageMixin, JSONResponseMixin, AjaxResponseMixin, DetailView):
    model = Article
    template_name = "knowledgebase/article_vote.html"
    _success_upvote_message = _("Thanks, glad we could help!")
    _success_downvote_message = _("We're sorry to hear that.")
    _error_message = _("There was a problem completing your request.")

    def get_context_data(self, **kwargs):
        context = super(ArticleVoteView, self).get_context_data(**kwargs)
        context['vote'] = self.kwargs['vote']
        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()

        if self._vote_article(request, article):
            self.messages.success(self._get_success_message())
        else:
            self.messages.success(self._error_message)

        return redirect('knowledgebase:article_detail', slug=article.slug)

    def get_ajax(self, request, *args, **kwargs):
        json_dict = {
            'message': _('Bad request.').encode('utf-8')
        }

        return self.render_json_response(json_dict, 400)

    def post_ajax(self, request, *args, **kwargs):

        if self._vote_article(request):
            message = self._get_success_message()
            status = 200
        else:
            message = self._error_message
            status = 500

        json_dict = {
            'message': message.encode('utf-8')
        }

        return self.render_json_response(json_dict, status)

    def put_ajax(self, request, *args, **kwargs):
        return self.get_ajax(request, *args, **kwargs)

    def delete_ajax(self, request, *args, **kwargs):
        return self.get_ajax(request, *args, **kwargs)

    def _get_success_message(self):
        if self.kwargs['vote'] == 'downvote':
            return self._success_downvote_message

        return self._success_upvote_message

    def _vote_article(self, request, article=None):
        try:
            # Retrieve token
            token = request.secretballot_token
            if request.user.is_authenticated():
                token = request.user.pk

            # Determine user vote
            vote = 1 if self.kwargs['vote'] == 'upvote' else -1

            # Add article vote
            article = self.get_object() if article is None else article
            article.add_vote(token, vote)

            return True

        except Exception:
            return False
