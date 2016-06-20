#-*- coding: utf-8 -*-
from django.db import models

class ExceptionLog(models.Model):
    exception_class = models.CharField(max_length=100, blank=True)
    exception_type = models.CharField(max_length=100, blank=True)
    exception_args = models.TextField(blank=True)
    exception = models.TextField(blank=True)
    request = models.TextField(blank=True)
    request_get = models.TextField(blank=True)
    request_post = models.TextField(blank=True)
    request_files = models.TextField(blank=True)
    request_path = models.CharField(max_length=200, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
