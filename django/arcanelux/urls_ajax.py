# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('arcanelux.ajax_apis',
    url(r'^get_model_query/$', 'get_model_query', name='get_model_query'),
)