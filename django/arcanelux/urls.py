from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^froala_editor/', include('froala_editor.urls')),

    # Apps Views
    url(r'^$', 'portfolio.views.list', name='index'),
    url(r'^career/$', 'blog.views.career', name='career'),
    url(r'^portfolio/', include('portfolio.urls', namespace='portfolio')),

    # Apps Ajax APIs
    url(r'^ajax/', include('arcanelux.urls_ajax', namespace='ajax')),
    url(r'^ajax/portfolio/', include('portfolio.urls_ajax', namespace='ajax_portfolio')),


    # Others
    url(r'^render_static/(.+)/$', 'arclib.django.static.render_static_file'),
    url(r'^render_static/$', 'arclib.django.static.render_static_file', name='render_static'),
    url(r'^url_reverse/$', 'arclib.django.static.url_reverse', name='url_reverse'),
    url(r'^url_reverse/(.+)/(.+)/$', 'arclib.django.static.url_reverse'),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (
            r'^media/(?P<path>.*)$',
            'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT
            }
        )
    )