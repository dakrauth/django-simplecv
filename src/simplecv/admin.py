import json
from django.db import models
from django.contrib import admin
from django.forms.widgets import Textarea

from .models import CV


class JSONTextarea(Textarea):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs["style"] = "font-family: monospace; width: 95%; min-height: 60em"

    def format_value(self, value):
        return json.dumps(json.loads(str(value)), indent=4)


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ["label", "user", "date_updated"]
    fields = ["user", "label", "date_created", "date_updated", "data"]
    readonly_fields = ["date_created", "date_updated"]
    formfield_overrides = {
        models.JSONField: {"widget": JSONTextarea},
    }
