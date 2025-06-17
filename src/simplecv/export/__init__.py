from io import BytesIO

from django.template.loader import render_to_string

from .todocx import convert as docx_convert
from .topdf import convert as pdf_convert


def txt_convert(cv, stream):
    content = render_to_string("simplecv/simplecv.txt", {"cv": cv})
    stream.write(content)
    return content


def export(stream, cv, kind):
    exporter = EXPORTERS.get(kind)

    if not stream:
        stream = BytesIO()

    exporter(cv, stream)
    return stream


EXPORTERS = {"docx": docx_convert, "pdf": pdf_convert, "txt": txt_convert}
