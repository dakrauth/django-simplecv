import textwrap
from django import template

register = template.Library()


@register.filter
def wrap(value, subsequent_indent=""):
    return "\n".join(textwrap.wrap(str(value), subsequent_indent=subsequent_indent))


@register.filter
def width(value, nchars):
    return "{:{}}".format(str(value), nchars)
