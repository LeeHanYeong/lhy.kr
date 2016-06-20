#-*- coding: utf-8 -*-
from datetime import datetime

from django.db import models

from froala_editor.fields import FroalaField

from arcanelux import get_file_path
from arcanelux.c import FORMAT_MONTH

from arclib.django.functions import imageinfo, day_to_string, datetime_to_string

def filepath_workimage(instance, filename):
    return get_file_path('work', filename)

class Platform(models.Model):
    title = models.CharField(max_length=100)
    icon_active = models.ImageField(upload_to='portfolio/platform/', blank=True)
    icon_inactive = models.ImageField(upload_to='portfolio/platform/', blank=True)

    def __unicode__(self):
        return self.title

    def json(self, is_active=None):
        data = {
            'id': self.id,
            'title': self.title,
        }
        if is_active is True:
            data['img_icon'] = imageinfo(self.icon_active)
        elif is_active is False:
            data['img_icon'] = imageinfo(self.icon_inactive)
        else:
            pass
        return data

class Project(models.Model):
    platform_list = models.ManyToManyField(Platform, related_name='platform_set')
    my_platform_list = models.ManyToManyField(Platform, related_name='my_platform_set')
    title = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.now(), blank=True)
    end_date = models.DateField(default=datetime.now(), blank=True)
    is_progress = models.BooleanField(default=False)
    project_type = models.CharField(max_length=100, blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    description = FroalaField(blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'프로젝트'
        verbose_name_plural = u'프로젝트 목록'
        ordering = ['-start_date']

    def json(self, show_description=False):
        data = {
            'id': self.id,
            'title': self.title,
            'start_date': day_to_string(self.start_date),
            'end_date': day_to_string(self.end_date),
            'period': '%s - %s' % (datetime_to_string(self.start_date, FORMAT_MONTH), datetime_to_string(self.end_date, FORMAT_MONTH) if not self.is_progress else datetime_to_string(datetime.now(), FORMAT_MONTH)),
            'is_progress': self.is_progress,
            'project_type': self.project_type,
            'short_description': self.short_description,
            # 'description': self.description,
        }
        data['platform_list'] = []
        for platform in self.platform_list.all():
            if platform in self.my_platform_list.all():
                data['platform_list'].append(platform.json(is_active=True))
            else:
                data['platform_list'].append(platform.json(is_active=False))

        if show_description:
            data['description'] = self.description
        return data

class ProjectImage(models.Model):
    project = models.ForeignKey(Project)
    image = models.ImageField(upload_to=filepath_workimage, blank=True)

    def __unicode__(self):
        return u'%s\'s Image (%s)' % (self.project.title, self.image.name)

    def json(self):
        data = {
            'id': self.id,
            'image': imageinfo(self.image),
        }
        return data