#-*- coding: utf-8 -*-
from arclog.models import ExceptionLog

def log_exception(func):
    def wrap(request, *args, **kwargs):
        try:
            # print 'log_exception try : %s' % (func.__name__)
            return func(request, *args, **kwargs)
        except Exception as e:
            print 'log_exception except : %s, %s' % (func.__name__, str(e.__class__))
            try:    exception_class = str(e.__class__)
            except: exception_class = 'get class failure'

            try:    exception_type = str(type(e))
            except: exception_type = 'get type failure'

            try:    exception_args = str(e.args)
            except: exception_args = 'get args failure'

            try:    exception = str(e)
            except: exception = 'get error failure'

            try:    str_request = str(request)
            except: str_request = 'get request failure'

            try:    str_request_get = str(request.GET)
            except: str_request_get = 'get request.GET failure'

            try:    str_request_post = str(request.POST)
            except: str_request_post = 'get request.POST failure'

            try:    str_request_files = str(request.FILES)
            except: str_request_files = 'get request.FILES failure'

            try:    str_request_path = str(request.path)
            except: str_request_path = 'get request.path failure'

            ExceptionLog.objects.create(
                exception_class=exception_class,
                exception_type=exception_type,
                exception_args=exception_args,
                exception=exception,
                request=str_request,
                request_get=str_request_get,
                request_post=str_request_post,
                request_files=str_request_files,
                request_path=str_request_path,
            )
            return func(request, *args, **kwargs)

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap