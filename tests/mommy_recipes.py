from __future__ import absolute_import, unicode_literals
from itertools import cycle

from django.contrib.auth.models import User

from model_mommy.recipe import Recipe, foreign_key, seq

from knowledgebase.models import Article, Category

definitions = [
    ''''# HTML

**Hypertext Markup Language**, a standardized system for tagging
text files to achieve font, color, graphic, and hyperlink effects on
*World Wide Web pages*.''',
    ''''# JavaScript

an **object-oriented** computer programming language commonly used to
create interactive effects within *web browsers*.''',
    ''''# Python

a *high-level* **general-purpose** _programming language_.''',
]

user = Recipe(
    User,
    email="jhon@example.com",
    is_active=True
)

category = Recipe(
    Category,
    title=seq('Category'),
    author=foreign_key(user),
    description=cycle('description'),
    _quantity=3
)

article = Recipe(
    Article,
    title=seq('Article'),
    author=foreign_key(user),
    category=foreign_key(category),
    content=cycle(definitions),
    _quantity=5
)
