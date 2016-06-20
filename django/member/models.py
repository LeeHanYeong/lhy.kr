#-*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

class ArcUserManager(BaseUserManager):
    def create_user(self, username, last_name, first_name, email,\
        nickname, password=None):
        user = self.model(
            username=username,
            last_name=last_name,
            first_name=first_name,
            email=email,
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password):
        user = self.model(
            username=username,
            last_name='Arc',
            first_name='Admin',
            email=email,
            nickname='ArcAdmin',
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class ArcUser(AbstractUser):
    # 이미 있는 것
    # username, first_name, last_name, email,
    # password, groups, user_permissions,
    # is_staff, is_active, is_superuser,
    # last_login, date_joined
    nickname = models.CharField(max_length=100, blank=True)

    objects = ArcUserManager()

    def __unicode__(self):
        return self.username