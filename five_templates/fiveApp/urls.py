from django.conf.urls import url
from fiveApp import views

#TEMPLATE TAGGING
app_name = 'fiveApp'

urlpatterns = [
        url(r'^relative/$',views.relative,name='relative'),
        url(r'^other/$',views.other,name='other'),
        url(r'^$',views.index,name='index'),
]
