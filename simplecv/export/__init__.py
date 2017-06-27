import os
from io import BytesIO
from django.template.loader import render_to_string
from .todocx import convert as docx_convert
from .topdf import convert as pdf_convert


def make_template_converter(template):
    def _converter(cv, stream):
        content = render_to_string(template, {'cv': cv})
        stream.write(content)
        return content
    return _converter


EXPORTERS = {
    'docx': docx_convert,
    'pdf': pdf_convert,
    'txt': make_template_converter('simplecv/simplecv.txt'),
    'html': make_template_converter('simplecv/simplecv.html')
}

all_exports_types = set(EXPORTERS.keys()) 

def export(stream, cv, kind):
    func = EXPORTERS.get(kind)
    if func is None:
        raise KeyError('Unknown exporter: "{}"'.format(kind))

    if not stream:
        stream = BytesIO()

    func(cv, stream)
    return stream
