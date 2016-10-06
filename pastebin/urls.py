
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.list.ListView import object_list, object_detail
from django.views.generic.create_update import create_object
from app.models import Pastebin

display_info = {'queryset': Pastebin.objects.all()}
create_info = {'model': Pastebin}


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', object_list, dict(display_info, allow_empty=True)),
    url(r'^(?P<object_id>\d+)/$', object_detail, display_info),
    url(r'^add/$', create_object, create_info),
]
