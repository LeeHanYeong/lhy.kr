#-*- coding: utf-8 -*-
from django.contrib import admin

from arclog.models import ExceptionLog

class ExceptionLogAdmin(admin.ModelAdmin):
    list_display = ['request_path', 'exception_class', 'exception_type', 'exception_args', 'request_get', 'request_post', 'request_files', 'created']

admin.site.register(ExceptionLog, ExceptionLogAdmin)