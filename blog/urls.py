from django.conf.urls.defaults import *
from django.conf import settings

from blog.plugins.RSS.rss import LatestPosts

urlpatterns = patterns('',


    url(r'^authors/', include('blog.plugins.custom_user.urls')),

    url(r'^twitter/', include('blog.plugins.twitter.urls')),

    url(r'^rss/', LatestPosts()),

    url(r'^', include('blog.core.urls')),     

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT }),


)


