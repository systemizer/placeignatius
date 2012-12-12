from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    (r'', include('placeignatius.main.urls')),
    (r'^admin/', include(admin.site.urls)),
)


urlpatterns += staticfiles_urlpatterns()
