# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 17:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import markupfield.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=200)),
                ('content', markupfield.fields.MarkupField(rendered_field=True, verbose_name='Content')),
                ('content_markup_type', models.CharField(choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown')], default='markdown', max_length=30)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'published')], default=0)),
                ('_content_rendered', models.TextField(editable=False)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', markupfield.fields.MarkupField(rendered_field=True, verbose_name='Description')),
                ('description_markup_type', models.CharField(choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown')], default='markdown', max_length=30)),
                ('_description_rendered', models.TextField(editable=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='django_knowledgebase.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]