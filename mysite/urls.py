from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls.views import *
from books.views import *


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^display_meta/$', display_meta),
    url(r'^current_datetime/$', current_datetime),
    url(r'^current_url_view/$', current_url_view),
    url(r'^search_form/$', search_form),
    url(r'^search/$', search),
)