from django.conf.urls.defaults import patterns, include, url

from engine import views

urlpatterns = patterns('',
    url(r'^logout/$', 'engine.views.logout',name='engine-logout'),
    url(r'^$', 'engine.views.index'),
)
