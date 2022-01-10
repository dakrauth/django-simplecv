import re
import json

from django import http
from django.shortcuts import render

from . import utils
from .models import CV
from .export import export


def set_content_disposition(response, filename, as_download=True):
    disposition = 'attachment' if as_download else 'inline'
    response['Content-Disposition'] = f'{disposition}; filename="{filename}"'


def cv_view(request, ext='html', **query_params):
    ext = ext.lower()
    if ext not in utils.content_types:
        raise http.Http404(f'Unknown CV conversion type: "{ext}"')

    try:
        cv = CV.objects.get(**query_params) if query_params else CV.objects.latest()
    except CV.DoesNotExist:
        raise http.Http404

    as_download = 'download' in request.GET
    filename = '{}-CV.{}'.format(re.sub(r'[^\w-]', '', cv.data['name']), ext)

    response = http.HttpResponse(content_type=utils.content_types[ext])
    if ext == 'docx' and as_download:
        set_content_disposition(response, filename, as_download)
        return export(response, cv, ext)

    elif ext == 'pdf':
        set_content_disposition(response, filename, as_download)
        return export(response, cv, ext)

    if as_download:
        set_content_disposition(response, filename)

    return export(response, cv, ext)
