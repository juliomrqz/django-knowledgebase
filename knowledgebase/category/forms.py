from __future__ import unicode_literals

from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'slug', 'description']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['slug'].required = False
