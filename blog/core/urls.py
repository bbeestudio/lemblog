from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('blog.plugins.core.views',

    url(r'^$', view=index, name='index'),

    url(r'^cats/$', view=cats, name='cat'),

    url(r'^cats/([^/]+)/$', view=cats, name='cat'),

    url(r'^tags/([^/]+)/$', view=tags, name='tag'),

    url(r'^arch/(\d+)/(\d+)/$', view=arch, name='arch'),

    url(r'^arch/(\d+)/$', view=arch, name='arch'),

    url(r'^arch/$', view=arch, name='arch'),

    url(r'^([^/]+)/$', view=detail, name='post'),
)
