from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#admin.autodiscover()
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^Jackpoint/', include('foo.urls')),
    url(r'^logout/$', 'engine.views.logoutpage',name='engine-logout'),
    url(r'^$', 'engine.views.index',name='engine-index'),
    #url(r'^X/$', 'X.views.index'),
    url(r'^invitation/$', 'invitation.views.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^invitation/create_invitation/$', 'invitation.views.create_invitation'),
    url(r'^invitation/inscription/$', 'invitation.views.invitation_inscription'),
    url(r'^invitation/inscription/validation/$', 'invitation.views.validation_inscription'),
    url(r'^hand/$', 'hand.views.index'),
    url(r'^X/$', 'X.views.index'),
    url(r'^hand/ask/$', 'hand.views.ask'),
    url(r'^hand/view/$','hand.views.index'),
    url(r'^hand/view/(?P<id>\d+)/$','hand.views.viewid'),
    url(r'^mp/(?P<id>\d+)/$','mp.views.index'),
    url(r'^jack/view/(?P<id>\d+)/$','jack.views.viewid'),
    url(r'^jack/edit/$','jack.views.editJack'),
    url(r'^place/view/(?P<id>\d+)/$','place.views.viewid'),
    url(r'^place/add/$','place.views.addplace'),
    url(r'^place/edit/$','place.views.editplace'),
    url(r'^event/view/(?P<id>\d+)/$','event.views.viewid'),
    url(r'^event/add/$','event.views.addevent'),
    url(r'^event/edit/$','event.views.editevent'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
