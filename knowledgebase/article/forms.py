from __future__ import unicode_literals

from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'category', 'status', 'tags']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False
