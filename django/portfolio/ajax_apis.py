#-*- coding: utf-8 -*-
import json
from django.db.models import Q

from arcanelux.decorator import api
from arclib.django import ArcReturnJSONObject

from portfolio.models import Platform, Project

@api
def list(request):
    pass