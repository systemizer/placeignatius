from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('placeignatius.main.views',
                       url(r'^$', 'index',name="index"),
                       url(r'^place/(?P<width>.*)/(?P<height>.*)/', 'place',name="place"),
)
