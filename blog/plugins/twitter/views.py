# -*- coding:utf-8 -*-
import oauth, httplib, time, datetime

try:
    import simplejson
except ImportError:
    try:
        import json as simplejson
    except ImportError:
        try:
            from django.utils import simplejson
        except:
            raise "Requires either simplejson, Python 2.6 or django.utils!"
import urllib2, urllib
from django.http import *
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.conf import settings

from blog.plugins.twitter.utils import *
from blog.plugins.twitter.models import TwitterAcc

CONSUMER = oauth.OAuthConsumer(CONSUMER_KEY, CONSUMER_SECRET)
CONNECTION = httplib.HTTPSConnection(SERVER)


def main(request):
     current_site = Site.objects.get(id=settings.SITE_ID)
     return HttpResponseRedirect('http://' +  current_site.domain + '/admin/twitter/')

def auth(request):
    "/auth/"
    if request.user.is_authenticated():
        token = get_unauthorised_request_token(CONSUMER, CONNECTION)
        auth_url = get_authorisation_url(CONSUMER, token)
        response = HttpResponseRedirect(auth_url)
        request.session['unauthed_token'] = token.to_string()   
        return response
    else:
        return HttpResponse("You are not authorized user!")

def unauth(request):
    if request.user.is_authenticated():
        response = HttpResponseRedirect(reverse('twitter_oauth_main'))
        request.session.clear()
        return response
    else:
        return HttpResponse("You are not authorized user!")

def return_(request):

    "/return/"
    unauthed_token = request.session.get('unauthed_token', None)
    if not unauthed_token:
        return HttpResponse("No un-authed token cookie")
    token = oauth.OAuthToken.from_string(unauthed_token)   
    if token.key != request.GET.get('oauth_token', 'no-token'):
        return HttpResponse("Something went wrong! Tokens do not match")
    access_token = exchange_request_token_for_access_token(CONSUMER, CONNECTION, token)
    request.session['access_token'] = access_token.to_string()
    access_token = request.session.get('access_token', None) 
    if not access_token:
        return HttpResponse("You need an access token!")
    token = oauth.OAuthToken.from_string(access_token)   
    auth = is_authenticated(CONSUMER, CONNECTION, token)
    if auth:
        # Load the credidentials from Twitter into JSON
        creds = simplejson.loads(auth)
        name = creds.get('screen_name', creds['screen_name'])
        acc = TwitterAcc.objects.filter(name=name)
        if not acc:
            t = TwitterAcc(name = name, PIN= token, enable = True).save()
    current_site = Site.objects.get(id=settings.SITE_ID)
    response = HttpResponseRedirect('http://'+  current_site.domain + '/admin/twitter/')
    return response

def ShortUrl(url_to_shorten, shortener = "http://bbee.su/api/shortener", query = "url" ):
    return urllib2.urlopen(shortener + '?' + urllib.urlencode({query: url_to_shorten})).read()

def twitit(twit):
    "/twit/"
    accounts = TwitterAcc.objects.filter(enable=True)
    for ac in accounts:
        access_token = ac.PIN
        if not access_token:
            return HttpResponse("You need an access token!")
        token = oauth.OAuthToken.from_string(access_token)   
        auth = is_authenticated(CONSUMER, CONNECTION, token)
        if auth:
            send = update_status(CONSUMER, CONNECTION, token, twit)
