from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.crazy88, name='crazy88'),
    url(r'^quote', views.quote, name='quote'),
]