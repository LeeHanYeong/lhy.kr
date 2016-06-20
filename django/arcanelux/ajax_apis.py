#-*- coding: utf-8 -*-
import json
from datetime import datetime

from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.db.models import Q

from arclib.django import ArcReturnJSONObject
from arcanelux.decorator import api

from portfolio.models import Platform, Project

@api
def get_model_query(request):
    query_dict = request.POST
    req_type = query_dict['type']

    str_value_dict = query_dict['value_dict']
    value_dict = json.loads(str_value_dict)

    jsondata = ArcReturnJSONObject(False, 'No data response')

    if req_type == 'project_list':
        year = value_dict.get('year', -1)
        platform_id = value_dict.get('platform_id', -1)

        if year == -1 and platform_id == -1:
            print '1'
            project_list = Project.objects.all()
        elif year == -1:
            print '2'
            project_list = Project.objects.filter(my_platform_list__id__exact=platform_id)
        elif platform_id == -1:
            print '3'
            if int(year) == datetime.now().year:
                project_list = Project.objects.filter(Q(start_date__year=year) | Q(end_date__year=year) | Q(is_progress=True))
            else:
                project_list = Project.objects.filter(Q(start_date__year=year) | Q(end_date__year=year))
        else:
            pass

        jsondata = ArcReturnJSONObject(True)
        jsondata.add_object('project_list', [project.json() for project in project_list])
    elif req_type == 'platform_list':
        platform_list = Platform.objects.all()

        jsondata = ArcReturnJSONObject(True)
        jsondata.add_object('platform_list', [platform.json() for platform in platform_list])

    return jsondata.json_response()
    # return HttpResponse('ok')
