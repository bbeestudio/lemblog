from django.conf.urls.defaults import *
from blog.plugins.RSS.rss import LatestPosts

feeds = {
    'rss': LatestPosts,
}

urlpatterns = patterns('',
    (r'^(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds['rss']}),
)
