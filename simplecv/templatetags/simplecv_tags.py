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


@register.filter(name='json')
def as_json(data, indent='2'):
    if not indent.isdigit():
        raise ValueError('json indent value must be an integer string')
    

    print('as_json data length: {}'.format(len(data)))
    result = json.dumps(data, indent=int(indent))
    print('as_json result length: {}'.format(len(result)))
    return result
