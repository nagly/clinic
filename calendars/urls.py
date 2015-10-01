from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$', 'calendars.views.hours'),
    url(r'^get/(?P<id>\d+)/$', 'calendars.views.hour'),
    url(r'^add/(?P<id>\d+)/$', 'calendars.views.add_patient'),
    url(r'^day/(?P<id>\d+)/$', 'calendars.views.date'),
    url(r'^(?P<id_godz>\d+)/signout/$', 'calendars.views.signout'),

)