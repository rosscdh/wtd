# -*- coding: UTF-8 -*-
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url

from .api import PageDiffOrCreate


urlpatterns = patterns('',
    url(r'^test_diff/', TemplateView.as_view(template_name='test/test_diff.html'), name='test_diff'),
    url(r'^wtd/', PageDiffOrCreate.as_view(), name='page_diff_or_create'),
)