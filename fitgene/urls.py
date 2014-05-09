from django.conf.urls import patterns,include,url
from django.contrib import admin
from fitgene import views

admin.autodiscover()

# urlpatterns = patterns('',
#                        url(r'^$', views.index, name='index'),
#                        url(r'^(?P<chr_no>\d+)/$', views.action, name='action'),
#                        )
