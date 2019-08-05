from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


app_name = 'SocialBoard'
urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^logout/$', logout, name='logout')
]