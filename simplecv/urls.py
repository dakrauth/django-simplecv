from django.urls import re_path
from . import views

app_name = 'simplecv'

urlpatterns = [
    re_path(r'^$', views.cv_view, name='simplecv'),
    re_path(r'^cv\.(\w+)$', views.cv_view, name='simplecv-format'),
    re_path(r'^docx/$', views.docx_view, name='docx-view'),
    re_path(r'^docx/html/$', views.docx_html_view, name='docx-html-view'),
]
