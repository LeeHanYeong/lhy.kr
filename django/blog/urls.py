from django.conf.urls import patterns, include, url
from django.contrib import admin
from smarturls import surl

from blog import views

urlpatterns = patterns('',
    # url(r'^/$', views.list, name='index'),
    # url(r'^list/$', views.list, name='list'),
    # surl('/<int:project_id>/', views.detail, name='detail'),
    # url(r'^(\d+)/$', views.detail, name='detail'),
)
