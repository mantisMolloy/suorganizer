from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^tag/$', tag_list, name='organizer_tag_list'),
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organsizer_tag_detail'),
    url(r'^startup/$', startup_list, name='organizer_startup_list'),
    url(r'^startup/(?P<slug>[\w\-]+)+/$', startup_detail, name='startup_detail'),
]
