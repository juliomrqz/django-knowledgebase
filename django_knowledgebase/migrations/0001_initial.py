# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
import markupfield.fields
import django.utils.timezone
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('content', markupfield.fields.MarkupField(rendered_field=True, verbose_name='Content')),
                ('content_markup_type', models.CharField(default='markdown', max_length=30, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown')])),
                ('_content_rendered', models.TextField(editable=False)),
                ('status', models.IntegerField(default=0, choices=[(0, 'draft'), (1, 'published')])),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=200, verbose_name='Description', blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(related_name='articles', to='django_knowledgebase.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
