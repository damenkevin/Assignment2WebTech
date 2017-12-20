from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', views.quote, name='quote'),
    #url(r'^crazy88', views.crazy88, name='crazy88'),
    url(r'^quote', views.quote, name='quote'),
    url(r'^quotes', views.quote_detail, name='quote_detail'),
]