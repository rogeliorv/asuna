from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asuna.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # grappelli URLS
    (r'^grappelli/', include('grappelli.urls')),
    # admin site
    (r'^admin/',  include(admin.site.urls)),
)
