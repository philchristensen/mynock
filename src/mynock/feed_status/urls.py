# mynock
# Copyright (c) 2011 Phil Christensen
#
#
# See LICENSE for details

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # Example:
    # (r'^mynock/', include('mynock.foo.urls')),
    url(r'^$', 'summary', name='status-page', prefix='mynock.feed_status.views'),
)
