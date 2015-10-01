from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/$', 'patients.views.profile_view'),
    url(r'^(?P<id>\d+)/medical_card/$', 'patients.views.medical_card'),
    url(r'^(?P<id>\d+)/history/$', 'patients.views.history'),
    #url(r'^(?P<id>\d+)/profil/$', 'patients.views.profile'),


)