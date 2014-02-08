from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^a/', include(admin.site.urls)),
    url(r'^', include('wtd.apps.core.urls', namespace='wtd')),
)
