from django.conf.urls import patterns, include, url

from portfolio import ajax_apis

urlpatterns = patterns('',
    url(r'^list/$', ajax_apis.list, name='list'),
)