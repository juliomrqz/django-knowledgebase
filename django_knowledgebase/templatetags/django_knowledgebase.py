from django import template

from ..base import choices


register = template.Library()


@register.filter
def article_status_text(value):
    """Get the text of a given status value"""
    return choices.STATUS[value]
