from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'URLShortener'
urlpatterns = [
    #ex: /URLShortener/
    url(r'^$', views.UserHomeRedirect, name='user_home'),
    url(r'^URLs/(?P<pk>\w+\d*)/createURL/request$', views.URLCreationCompleteRedirect, name='urlcreaterequest'),
    url(r'^URLs/(?P<pk>\w+\d*)/createURL/$', views.URLCreateView, name='urlcreate'),
    url(r'^URLs/(?P<user_id>\w+\d*)/(?P<pk>\w+\d*)/deleteURL/$', views.URLDeleteView.as_view(), name='urldelete'),
    url(r'^URLs/(?P<pk>\w+\d*)/$', views.UserURLDetail, name='userurls'),
    url(r'^URLs/$', views.UserHomeRedirect, name='user_home'),
    url(r'(?P<user_id>\w+\d*).(?P<pk>\w{1,10})/$', views.URLRedirect, name='url_redirect'),

]    

urlpatterns += staticfiles_urlpatterns()