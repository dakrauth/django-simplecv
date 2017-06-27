from django.conf.urls import url
from . import views

app_name = 'simplecv'

urlpatterns = [
    url(r'^$', views.cv_view, name='simplecv'),
    url(r'^cv\.(\w+)$', views.cv_view, name='simplecv-format'),
    url(r'^docx/$', views.docx_view, name='docx-view'),
    url(r'^docx/html/$', views.docx_html_view, name='docx-html-view'),
]
