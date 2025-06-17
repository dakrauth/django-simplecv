import re

from django import http
from django.views.generic import DetailView

from . import utils
from .models import CV
from .export import export


class CVDetailView(DetailView):
    model = CV
    queryset = CV.objects.all()
    user_name = None
    label = None
    context_object_name = "cv"
    template_name = "simplecv/simplecv.html"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        user_name = self.user_name or self.kwargs.get("user_name")
        label = self.label or self.kwargs.get("labels")

        if not (user_name and label):
            raise http.Http404("Missing user_name and label")

        queryset = queryset.filter(user__username=user_name, label=label)
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except CV.DoesNotExist:
            raise http.Http404("No CV found matching the query")

        return obj


class CVDetailExportView(CVDetailView):
    content_types = {
        "pdf": "application/pdf",
        "txt": "text/plain; charset=utf-8",
        "docx": ("application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
        "json": "application/json",
    }

    def set_content_disposition(self, response, filename, as_download=True):
        disposition = "attachment" if as_download else "inline"
        response["Content-Disposition"] = f'{disposition}; filename="{filename}"'

    def render_to_response(self, context):
        cv = context["cv"]
        ext = self.kwargs.get("ext").lower()
        if ext not in self.content_types:
            raise http.Http404(f'Unknown CV conversion type: "{ext}"')

        as_download = "download" in self.request.GET
        filename = "{}-CV.{}".format(re.sub(r"[^\w-]", "", cv.data["name"]), ext)

        response = http.HttpResponse(content_type=self.content_types[ext])
        if ext == "docx" and as_download:
            self.set_content_disposition(response, filename, as_download)
            return export(response, cv, ext)

        elif ext == "pdf":
            self.set_content_disposition(response, filename, as_download)
            return export(response, cv, ext)

        if as_download:
            self.set_content_disposition(response, filename)

        return export(response, cv, ext)
