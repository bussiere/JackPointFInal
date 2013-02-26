from django.conf.urls.defaults import patterns, include, url

from X import views

 urlpatterns =patterns('views',
    url(r'^logout/$', view1, name='view1')
)