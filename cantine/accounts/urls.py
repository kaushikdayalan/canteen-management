from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url('home4/', views.home, name='home'),
    #url(r'^$', views.home, name='home'),
    #url(r'^signup/$', views.signup, name='signup'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
       # views.activate, name='activate'),
    #url(r'^$', views.activate, name='activate'),  

    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    
]