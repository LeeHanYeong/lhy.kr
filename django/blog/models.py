#-*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from froala_editor.fields import FroalaField

from arcanelux import get_file_path, dirpath_upload_file
from arcanelux.c import FORMAT_MONTH

from arclib.django.functions import imageinfo, day_to_string, datetime_to_string

class ArticleCategory(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    content = FroalaField(blank=True)
    file = models.FileField(blank=True, upload_to=dirpath_upload_file)

    def __unicode__(self):
        return self.title


class Career(models.Model):
    title = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    content = FroalaField(blank=True)

    def __unicode__(self):
        return self.title