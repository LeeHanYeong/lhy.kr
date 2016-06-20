# decorator
from arclib.django.decorators import api as arc_api, exception_json
from arclog.decorators import log_exception

def api(func):
    @arc_api
    @exception_json
    @log_exception
    def wrap(request, *args, **kwargs):
        return func(request, *args, **kwargs)
    return wrap