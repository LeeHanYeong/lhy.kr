#-*- coding: utf-8 -*-
import os
from dateutil import tz
from datetime import datetime

# FORMAT
FORMAT_DATE = '%Y.%m.%d-%H.%M.%S'
FORMAT_MONTH = '%Y.%m'
FORMAT_DATE_DIR = '%Y.%m.%d'

# FILE PATH
def __get_dir_path(dir_path):
    now = datetime.now(tz.tzlocal())
    date_path = now.strftime(FORMAT_DATE_DIR)
    cur_path = os.path.join(dir_path, date_path)

    # if not os.path.exists(cur_path):
    #     os.makedirs(cur_path)

    return cur_path

def get_file_path(dir_path, filename, prefix=None):
    cur_dir_path = __get_dir_path(dir_path)

    file_name, file_ext = os.path.splitext(filename)
    now = datetime.now(tz.tzlocal())
    now_string = now.strftime(FORMAT_DATE)
    if prefix is not None:
        now_string = '%s-%s' % (prefix, now_string)

    file_path = '%s%s' % (now_string, file_ext)

    return os.path.join(cur_dir_path, file_path)

def dirpath_upload():
    return __get_dir_path('upload')

def dirpath_upload_file():
    return __get_dir_path('upload_file')