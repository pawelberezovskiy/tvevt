from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail,GetUser

urlpatterns = patterns('main.views',
    url(r'^$', 'api_root'),
    url(r'^user$', GetUser.as_view(), name='get-user'),
    url(r'^users/?age=(?P<age>\d+)$', UserList.as_view(), name='user-list-filtered'),
    url(r'^users$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<email>[\w\d\@\.]+)$', UserDetail.as_view(), name='user-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
