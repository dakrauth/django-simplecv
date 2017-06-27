import re
import json
from django import http
from django.shortcuts import render
from pydocx import PyDocX
from .utils import load_cv, content_types
from .export import export


def set_content_disposition(response, filename, as_download=True):
    response['Content-Disposition'] = '{}; filename="{}"'.format(
        'attachment' if as_download else 'inline',
        filename
    )


def cv_view(request, ext='html'):
    #import ipdb; ipdb.set_trace()
    ext = ext.lower()
    if ext not in content_types:
        raise http.Http404('Unknown CV conversion type: "{}"'.format(ext))

    as_download = 'download' in request.GET
    cv = load_cv()
    filename = '{}-CV.{}'.format(re.sub(r'[^\w-]', '', cv['name']), ext)

    response = http.HttpResponse(content_type=content_types[ext])
    if ext == 'docx':
        if as_download:
            set_content_disposition(response, filename, as_download)
            return export(response, cv, ext)

    elif ext == 'pdf':
        set_content_disposition(response, filename, as_download)
        return export(response, cv, ext)

    if as_download:
        set_content_disposition(response, filename)

    return export(response, cv, ext)


def docx_view(request):
    return render(request, 'simplecv/docx.html', {})


def docx_html_view(request):
    cv = load_cv()
    stream = export(None, cv, 'docx')
    return http.HttpResponse(PyDocX.to_html(stream))
