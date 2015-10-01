from django.conf.urls import patterns, include, url
from django.contrib import admin

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^users/', include('patients.urls')),
    url(r'^articles/', include('articles.urls')),
     #url(r'^$', 'patients.views.home', name='home'),
    url(r'^$', 'clinic.views.home', name='home'),

    # url(r'^thank-you/$', 'patients.views.thankyou', name='thankyou'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^calendar/', include('calendars.urls')),

    #user auth urls
    url(r'^login/$', 'clinic.views.login'),
    url(r'^auth/$', 'clinic.views.auth_view'),
    url(r'^logout/$', 'clinic.views.logout'),
    url(r'^loggedin/$', 'clinic.views.loggedin'),
    url(r'^invalid/$', 'clinic.views.invalid_login'),
    url(r'^register/$', 'clinic.views.register_user'),
    url(r'^register_success/$', 'clinic.views.register_success'),
    url(r'^doctors/$', 'clinic.views.doctors_view')
)
