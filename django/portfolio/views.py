#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from portfolio.models import Project

def list(request):
    return render_to_response('portfolio/list.html', RequestContext(request))

def detail(request, project_id):
    project = Project.objects.get(id=project_id)
    d = {
        'project': project,
    }
    return render_to_response('portfolio/detail.html', d, RequestContext(request))