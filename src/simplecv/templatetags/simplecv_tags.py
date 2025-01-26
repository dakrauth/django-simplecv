import textwrap
from django import template

register = template.Library()


@register.filter
def wrap(value, subsequent_indent_len="0"):
    subsequent_indent = " " * int(subsequent_indent_len)
    return "\n".join(textwrap.wrap(str(value), subsequent_indent=subsequent_indent))


@register.filter
def width(value, nchars):
    return "{:{}}".format(str(value), nchars)


@register.simple_tag
def underline(char, *bits):
    line = " ".join(bits)
    ul = char * len(line)
    return f"{line}\n{ul}"
