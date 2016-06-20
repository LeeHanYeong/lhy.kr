#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from portfolio.models import Project
from blog.models import Career

def career(request):
    c = Career.objects.last()
    d = {
        'career': c,
    }
    return render_to_response('career/career.html', d, RequestContext(request))