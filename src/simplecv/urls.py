from django.urls import path
from . import views

app_name = "simplecv"

urlpatterns = [
    path("<str:user_name>/<str:label>/", views.CVDetailView.as_view(), name="cv"),
    path(
        "<str:user_name>/<str:label>.<str:ext>",
        views.CVDetailExportView.as_view(),
        name="format"
    ),
]
