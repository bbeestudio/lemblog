from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('blog.plugins.custom_user.views',

    url(r'^([^/]+)/posts/$', view=get_user_posts, name='user_posts'),
    
    url(r'^([^/]+)/$', view=user, name='user'),

)

