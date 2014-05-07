from django.conf.urls import patterns, include, url

from django.contrib import admin
from fitgene import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loc_fit_gene.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^fitgene/',views.index, name='index'),
)
