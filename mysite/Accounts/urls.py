from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'logout/$', views.LogoutView, name='logout'),
    url(r'create_user/$', views.CreateUserView.as_view(), name='createuser')
]