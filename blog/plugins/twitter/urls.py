from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('blog.plugins.twitter.views',
    
    url(r'^$',view=main, name='twitter_oauth_main'),

    url(r'^auth/$', view=auth, name='twitter_oauth_auth'),

    url(r'^unauth/$', view=unauth, name='twitter_oauth_unauth'),

    url(r'^return/$', view=return_, name='twitter_oauth_return'),

    url(r'^twitit/$', view=twitit, name='twitter_oauth_twitit'),

)
