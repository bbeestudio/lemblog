from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from blog.core.views import maintenance,index

from models import Settings

class AvailableMiddleware:
    def process_request(self, request):
        if Settings.objects.all().count()!=0:
            disable = Settings.objects.all()[0].disable
            if not request.path.startswith('/admin/') and disable:
                return maintenance(request)
        else:
            return None
        return None
