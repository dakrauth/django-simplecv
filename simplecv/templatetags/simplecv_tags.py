import json
import textwrap
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def wrap(value, subsequent_indent=''):
    return '\n'.join(textwrap.wrap(
        str(value),
        subsequent_indent=subsequent_indent
    ))


@register.filter
def width(value, nchars):
    return '{:{}}'.format(str(value), nchars)
