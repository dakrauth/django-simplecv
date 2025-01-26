from django.contrib import admin

from . import models as cv

PreferredInline = admin.TabularInline


class SkillInline(PreferredInline):
    model = cv.Skill
    extra = 1


class LinkInline(PreferredInline):
    model = cv.Link
    extra = 1


class EducationInline(admin.StackedInline):
    model = cv.Education
    extra = 1


class OrganizationInline(admin.StackedInline):
    model = cv.Organization
    extra = 1


class PositionInline(admin.StackedInline):
    model = cv.Position
    extra = 1


@admin.register(cv.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["name", "cv"]
    fields = ["cv", "name", "previous", "staffed_by", "location"]
    inlines = [PositionInline]


@admin.register(cv.CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ["label", "user", "date_updated"]
    fields = [
        "user",
        "label",
        "full_name",
        "email",
        "phone",
        "summary",
        "image",
        "data",
        "date_created",
        "date_updated",
    ]
    readonly_fields = ["date_created", "date_updated"]

    inlines = [
        SkillInline,
        LinkInline,
        EducationInline,
        OrganizationInline,
    ]
