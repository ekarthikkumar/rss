from django.conf.urls import patterns, include, url
from rss.views import LatestFeed
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^s/$', 'jquery.views.home'),
    url(r'^feeds/rss/(?P<tag_name>[\w]+)/$', LatestFeed()),
    url(r'^admin/', include(admin.site.urls)),
)
