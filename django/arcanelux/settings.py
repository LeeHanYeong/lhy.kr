#-*- coding: utf-8 -*-
from arcanelux import dirpath_upload

# DIR Path
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


FROALA_UPLOAD_PATH = dirpath_upload()
FROALA_EDITOR_PLUGINS = ('font_size', 'font_family', 'colors', 'block_styles', 'video', 'tables', 'media_manager', 'lists', 'file_upload', 'char_counter', 'urls', 'fullscreen', 'inline_styles', 'entities')

TEMPLATE_DIRS = (
    TEMPLATE_DIR,
)
STATICFILES_DIRS = (
    STATIC_DIR,
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # AllAuth
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',

    'froala_editor',

    # Apps
    'arclog',
    'member',
    'portfolio',
    'blog',
)

AUTH_USER_MODEL = 'member.ArcUser'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# django-allauth
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': False,
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',

                # allauth specific context processors
                # 'allauth.account.context_processors.account',
                # 'allauth.socialaccount.context_processors.socialaccount',

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

SECRET_KEY = '&^m0o(qlo9r*j5vi%0wzpj24l08cfzly^e-+c@ddyxq&j#)*li'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

ROOT_URLCONF = 'arcanelux.urls'
WSGI_APPLICATION = 'arcanelux.wsgi.application'

SITE_ID = 1
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True
